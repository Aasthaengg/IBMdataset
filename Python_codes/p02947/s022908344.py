N = int(input())
strings = {}
for i in range(N):
    s = ''.join(sorted(input()))
    if s in strings.keys():
        strings[s] += 1
    else:
        strings[s] = 1

ans = 0
for s in strings:
    x = strings[s]
    ans += x * (x-1) // 2

print(ans)
