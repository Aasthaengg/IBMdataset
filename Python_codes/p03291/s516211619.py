s = input()

dp_prev = [1, 0, 0, 0]

MOD_BASE = 1000000007

for c in s:
    dp_new = [dp_prev[i] for i in range(0, 4)]
    for i in range(0, 4):
        if c == "A":
            dp_new[1] = dp_prev[0] + dp_prev[1]

        elif c == "B":
            dp_new[2] = dp_prev[1] + dp_prev[2]

        elif c == "C":
            dp_new[3] = dp_prev[2] + dp_prev[3]

        else:
            dp_new[0] = dp_prev[0] * 3
            dp_new[1] = dp_prev[0] + dp_prev[1] * 3
            dp_new[2] = dp_prev[1] + dp_prev[2] * 3
            dp_new[3] = dp_prev[2] + dp_prev[3] * 3
            
    dp_prev = [x % MOD_BASE for x in dp_new]

ans = dp_prev[3]
print(ans)
