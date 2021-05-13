N=int(input())
a=[0]
for _ in range(N):
    a.append(int(input()))
i=1
cnt=1
while a[i]!=2:
    i=a[i]
    cnt+=1
    if cnt>N:
        print(-1)
        break
else:
    print(cnt)
