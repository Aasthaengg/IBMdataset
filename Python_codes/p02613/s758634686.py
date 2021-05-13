n = int(input())
s = [input() for i in range(n)]
ans = ["AC", "WA", "TLE", "RE"]
for i in range(4):
    char = ans[i]
    print(ans[i] + " x " + str(s.count(char)))
