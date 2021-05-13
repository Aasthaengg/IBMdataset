K = int(input())
A,B = map(int,input().split())
s = A // K
e = B // K + 1
ans = "NG"
for i in range(s,e):
  if A <= K * i <= B:
    ans = "OK"
    break
    
print(ans)