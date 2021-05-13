H, W = map(int, input().split())
C = []
ans = ""
for h in range(H):
    row = input()
    ans += row + "\n" + row + "\n"

print(ans)
