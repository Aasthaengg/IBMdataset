n = int(input())
ans = 0
if ((n-1)%2==0):
    ans = (n)*((n-1)//2)
else:
    ans = (n)*((n-1)//2) + n//2
print(ans)