N=int(input())
p=list(map(int, input().split()))
p = [0] + p
ans = 0
ids = []
flag = 0
if N == 2:
    i=1
    if p[i]==i or p[i+1]==i+1:
        print(1)
        exit()
for i in range(1, N):
    if flag:
        flag = 0
        continue
    if p[i]==i:
        if p[i+1]==i+1:
            # ids.append((i, i+1))
            ans += 1
            flag = 1
            continue
        else:
            # ids.append((i, i+1))
            ans += 1
if p[N] == N and not flag:
    # ids.append((N-1, N))
    ans += 1
print(ans)
