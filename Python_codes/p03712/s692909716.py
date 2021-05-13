H, W = list(map(lambda x: int(x), input().split(" ")))
A = []
A.append("#" * (W + 2))
for i in range(H):
  A.append("#" + input() + "#")
A.append("#" * (W + 2))

print("\n".join(A))