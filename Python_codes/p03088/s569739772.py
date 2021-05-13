N = int(input())
mod = int(1e+9 + 7)

options = ["A", "C", "G", "T"]
dp = [{options[i] + options[j] + options[k]: 0 for i in range(len(options)) for j in range(len(options)) for k in range(len(options))} for _ in range(N+1)]
keys = list(dp[0].keys())

dp[0]["TTT"] = 1

for i in range(N):
    for key in keys:
        for option in options:
            if key[1] == "A" and key[2] == "G" and option == "C":
                continue
            if key[0] == "A" and key[2] == "G" and option == "C":
                continue
            if key[1] == "G" and key[2] == "A" and option == "C":
                continue
            if key[1] == "A" and key[2] == "C" and option == "G":
                continue
            if key[0] == "A" and key[1] == "G" and option == "C":
                continue
            
            dp[i+1][key[1:3] + option] += dp[i][key]
            dp[i+1][key[1:3] + option] = dp[i+1][key[1:3] + option] % mod

print(sum(list(dp[-1].values()))%mod)