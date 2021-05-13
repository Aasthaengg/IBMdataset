n, q = map(int, input().split())
s = input()
d = [0]
for i in range(1, len(s)):
    d.append(d[-1] + (s[i-1:i+1] == 'AC'))
for _ in range(q):
    l, r = map(lambda x: int(x) - 1, input().split())
    if s[l] == 'C':
        l += 1
    print(d[r] - d[l])
