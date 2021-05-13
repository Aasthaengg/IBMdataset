# 「移動されるものとされないもの」という区分け
# 最も長く数字が並ぶものを探すというのはできていたんだけどな...
N = int(input())
P = [int(input()) for i in range(N)]

Q = [-1 for i in range(N)]
for i in range(N):
    Q[P[i]-1]=i

k = 1
i = 1
while i < N:
    cnt = 0
    while(i < N and Q[i-1] < Q[i]):
        cnt += 1
        i += 1
    k = max(k, cnt+1)
    i += 1

print(N - k)
