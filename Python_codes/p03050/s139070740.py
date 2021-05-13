n = int(input())
ans = 0
i = 1
while(n>(i+1)*i):
  if (n-i)%i==0:
    ans += (n-i)//i
  i += 1
print(ans)