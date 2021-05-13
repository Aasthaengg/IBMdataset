N = int(input())

s = 0
ans = []
for i in range(1, N + 1):
    ans.append(i)
    s += i
    if s >= N:
        break

diff = s - N
if diff != 0:
    ans.remove(diff)
for a in ans:
    print(a)
