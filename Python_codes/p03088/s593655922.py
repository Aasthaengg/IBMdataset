n = int(input())
mod = 10**9 + 7
acgt = ["A", "C", "G", "T"]
dp = {acgt[i]+acgt[j]+acgt[k]: 1 for i in range(4) for j in range(4) for k in range(4)}
dp["AGC"] = 0
dp["ACG"] = 0
dp["GAC"] = 0

for i in range(n-3):
    next_dp = {key: 0 for key in dp.keys()}
    for key, val in dp.items():
        for item in acgt:
            next_key = key + item
            if next_key[1:] == "AGC" or next_key[1:] == "ACG" or next_key[1:] == "GAC":
                continue
            elif next_key[0] + next_key[2:] == "AGC" or next_key[:2] + next_key[3] == "AGC":
                continue
            else:
                next_dp[next_key[1:]] = (next_dp[next_key[1:]] + val) % mod
    dp = next_dp
print(sum(dp.values()) % mod)