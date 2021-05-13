H, W = map(int, input().split())
A = ["#" * (W + 2)]
A.extend(["#" + input() + "#" for _ in range(H)])
A.append("#" * (W + 2))
print("\n".join(A))