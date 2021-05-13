N=int(input())
count=0
ans='No'

for i in range(N):
    d,e = map(int,input().split())
    if d==e:
        count += 1
        if count == 3:
            ans='Yes'
    else:
        count = 0

print(ans)
