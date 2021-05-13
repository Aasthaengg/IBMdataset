


"""
例２
3 2 5 1 4 6
5と6については昇順になっているので、4,3,2,1の順で配列の先頭に移動させればよい

↑のように考えると、既に並んでいる部分以外を適切な順で動かせばよいので、既に昇順のもので一番長いものをNから引くとよい？

"""

N = int(input())
P = [int(input()) for _ in range(N)]



idxs = [None] * N
for i,p in enumerate(P):
    idxs[p-1] = i

ans = N - 1

cnt = 1

for i in range(1,N):
    if idxs[i] > idxs[i-1]:
        cnt +=1
    else:
        ans = min(ans, N - cnt)
        cnt = 1

ans = min(ans, N - cnt)

print(ans)