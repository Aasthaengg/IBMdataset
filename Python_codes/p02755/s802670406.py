import math
A,B = map(int,input().split())

ans = ""
for i in range(1,1251):
  a = math.floor(i * 0.08)
  b = math.floor(i * 0.1)
  if a == A and b == B:
    ans = i
    break
    
print(ans if ans != "" else -1)