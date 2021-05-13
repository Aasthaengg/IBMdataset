N = int(input())
S = input()
direction = [{"E": 0, "W": 0} for _ in range(N + 1)]  # direcion[i]["E"] ... i番目までにEを向いている人数
ans = N
for i in range(N):
    direction[i + 1]["E"] = direction[i]["E"] + (1 if S[i] == "E" else 0)
    direction[i + 1]["W"] = direction[i]["W"] + (1 if S[i] == "W" else 0)
for i in range(N):
    ans = min(ans, direction[i]["W"] + direction[N]["E"] - direction[i + 1]["E"])
print(ans)
