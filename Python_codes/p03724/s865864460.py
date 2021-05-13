n,m = map(int,input().split())
cnt = [0]*n
for _ in range(m):
    a,b = map(int,input().split())
    a,b = a-1,b-1
    cnt[a]+=1
    cnt[b]+=1
for i in range(n):
    if cnt[i]&1:
        print("NO")
        break
else:
    print("YES")