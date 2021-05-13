N = int(input())
s = input()
t = input()
sameLen = 0
for i in range(N):
    if s[i:] == t[: N - i]:
        sameLen = N - i
        break
    else:
        continue
if sameLen == 0:
    print(2 * N)
else:
    print(2 * N - sameLen)