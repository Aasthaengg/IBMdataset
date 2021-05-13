d = int(input())
x = abs(25 - d)
ans = "Christmas"
for _ in range(x):
    ans = " ".join([ans, "Eve"])
print(ans)