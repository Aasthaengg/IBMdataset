H,W = map(int,(input().split()))
ans = [["#"]*(W+2) for _ in range(H+2)]
for i in range(H):
    a = list(input())
    ans[i+1][1:1+W] = a
for i in range(H+2):
    out = "".join(ans[i])
    print(out)