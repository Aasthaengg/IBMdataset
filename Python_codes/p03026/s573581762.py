from collections import deque
N = int(input())
ad_ls = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a,b = a-1,b-1
    ad_ls[a].append(b)
    ad_ls[b].append(a)
c_ls = list(map(int, input().split()))
c_ls.sort(reverse=True)
c_q = deque(c_ls)

# d_ls[i] := 0idxでi番目の頂点に書く数字
d_ls = [0] * N

q = deque()
q.append(0)
d_ls[0] = c_q.popleft()
while q:
    now = q.popleft()
    for nex in ad_ls[now]:
        if d_ls[nex] == 0:
            d_ls[nex] = c_q.popleft()
            q.append(nex)

print(sum(c_ls) - max(c_ls))
print(*d_ls)