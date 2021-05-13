import math
A,B,C = map(int,input().split())

ans = 0
while(1):
  tmp_A,tmp_B,tmp_C = A,B,C
  if((tmp_A%2 == 1)or(tmp_B%2 == 1)or(tmp_C%2 == 1)):
    break   
  A,B,C = (tmp_B+tmp_C)//2, (tmp_C+tmp_A)//2, (tmp_A+tmp_B)//2
  if((tmp_A == A)and(tmp_B == B)and(tmp_C == C)):
    ans = -1
    break
  ans += 1

print(ans)  