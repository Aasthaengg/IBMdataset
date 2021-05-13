def resolve():
    H, W = map(int, input().split())
    ans = []
    for _ in range(H):
        a = input()
        ans.append(a)
    print("#"*(W+2))
    for j in range(H):
        print("#"+ans[j]+"#")
    print("#"*(W+2))
resolve()