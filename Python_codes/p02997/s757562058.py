def main():
    n, k = map(int, input().split())
    mx = (n-1)*(n-2)//2
    if mx < k:
        print(-1)
        return
    ans = []
    for i in range(n-1):
        ans.append([i+1,n])     # star graph
    add = mx - k
    edge = []
    for i in range(n-1):
        for j in range(i):
            edge.append([i+1, j+1]) # complete graph
    for i in range(add):
        ans.append(edge[i])         # add本のedgeを追加
    m = len(ans)
    print(m)
    for i in range(m):
        print(*ans[i])

main()
