n = int(input())
a= list(map(int, input().split()))
before=a.pop(0)
ans=0
for i in a:
    if i==before:
        before=100000
        ans+=1
    else:
        before=i
print(ans)