N, X = map(int,input().split())
lst = list(map(int,input().split()))

cnt = 1
now = 0
for i in range(N):
    l = now + lst[i]
    if l > X:
        break
    else:
        cnt += 1
        now = l
    

print(cnt)