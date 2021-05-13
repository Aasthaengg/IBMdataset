n=int(input())
ans = 0
a = n//2
for i in range(1,a+1):
    if i != n-i:
        ans+=1
print(ans)