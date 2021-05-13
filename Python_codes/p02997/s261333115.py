


N,K = map(int, input().split())

"""
ノード１にノード２からNまでをつなぐ時が、距離２の組を最大にできるつなぎ方（のはず）で、nCk(N-1, 2)組できる。
あとはKがひとつ減るごとに、２～Nの間に辺を追加位していけばよいか

"""
if (N-1)*(N-2)//2 < K:
    print(-1)
    exit()


print(N-1 + ((N-1)*(N-2)//2 - K))
for i in range(2, N+1):
    print(1, i)

cnt = N-1
for i in range(2, N+1):
    for j in range(i+1, N+1):
        if cnt >= N-1 + ((N-1)*(N-2)//2 - K):
            exit()
        print(i,j)
        cnt += 1