n=int(input())
p=list(map(int,input().split()))
sort_p=sorted(p)
cnt=0

for i in range(n):
    if sort_p[i]!=p[i]:
        cnt+=1

if cnt<=2:
    print('YES')
else:
    print('NO')