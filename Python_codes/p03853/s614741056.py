H, W = map(int, input().split())

ans = []

for i in range(H):
    tmp = input()
    ans.append(tmp)
    ans.append(tmp)

print(*ans, sep="\n")