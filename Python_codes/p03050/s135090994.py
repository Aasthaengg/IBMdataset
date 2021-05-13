n = int(input())
x = int((n+1)**0.5)-1
ans = 0
for i in range(1,x+1):
  if (n-i)%i == 0:
    ans += (n-i)//i
print(ans)