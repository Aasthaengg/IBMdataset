n=int(input())
li=list(map(int, input().split()))
ans="Yes"
h=li[0]
for i in range(1,n):
    if h-li[i]>=2:
        ans="No"
        break
    h=max(h,li[i])
print(ans)