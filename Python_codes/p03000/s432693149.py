n,x = map(int,input().split())
l = list(map(int,input().split()))
cnt = 1
for i in range(n):
    if x>=l[i]:
        cnt += 1
        x = x - l[i]
    else:
        break
print(cnt)