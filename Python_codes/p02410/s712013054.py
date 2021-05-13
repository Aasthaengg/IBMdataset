n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

vec = []
for _ in range(m):
    vec.append(int(input()))

result = []
for line in mat:
    c = sum([line[i] * vec[i] for i in range(m)])
    result.append(c)

print("\n".join(map(str, result)))
