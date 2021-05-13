H, W = map(int, input().split())
A = [["#"]+list(input())+["#"] for _ in range(H)]

print("#"*(W+2))
for h in range(H):
    for w in range(len(A[h])):
        print(A[h][w], end="")
    print()
print("#"*(W+2))