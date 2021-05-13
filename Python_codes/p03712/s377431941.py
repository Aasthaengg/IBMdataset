H, W = map(int, input().split())
A = ["#"+str(input())+"#" for _ in range(H)]
res = "#" * (W+2)
print(res)
for i in range(H):
    print(A[i])
print(res)