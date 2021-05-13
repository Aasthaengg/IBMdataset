a, b=map(int, input().split())
ans=0

for num in range(a, b+1):
    num=str(num)
    if num[0]==num[-1] and num[1]==num[-2]:
        ans+=1

print(ans)