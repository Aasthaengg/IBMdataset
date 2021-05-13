s, t = [input() for i in range(2)]
ans = float("inf")
for i in range(len(s) - len(t)+1):
        cnt = 0
        for j in range(len(t)):
                if s[i + j] != t[j]:
                        cnt += 1
        if ans  > cnt:
                ans = cnt
print(ans)       