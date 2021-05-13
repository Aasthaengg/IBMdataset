def smax(s1, s2):
    if s1=="N":
        if s2[0]=="N":
            return "N"
        else:
            return s2
    if s2[0] == "N":
        return s1
    l1 = len(s1)
    l2 = len(s2)
    if l1 == l2:
        return max(s1, s2)
    if l1 > l2:
        return s1
    return s2

hon = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
n, m = map(int, input().split())
aa = list(map(int, input().split()))
dp = ["N"] * (n + 1)
dp[0]=""
for i in range(2, n + 1):
    for a in aa:
        if i - hon[a] < 0: continue
        dp[i] = smax(dp[i], dp[i - hon[a]] + str(a))
print(dp[-1])
