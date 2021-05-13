def task(probs):
    n = len(probs)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i, p in enumerate(probs, start=1):
        state = 0
        for j in range(i + 1):
          #print(state, p, 1-p, dp[j])
          curr = dp[j]
          dp[j] = (curr * (1 - p)) + state
          state =  curr * p

    return sum(dp[(n + 1) // 2:])


n = input()  # n
probs = [float(x) for x in input().split()]
print(task(probs))