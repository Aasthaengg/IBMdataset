n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
x = []
for _ in range(m):
    b, c = map(int, input().split())
    x.append([b, c])

x.sort(key=lambda p: p[1], reverse=True)

ret = 0
for b, c in x:
    if not a:
        break
    if c > a[-1]:
        while c > a[-1]:
            ret += c
            a.pop()
            b -= 1
            if b == 0:
                break
            if not a:
                break
    else:
        break

print(ret + sum(a))

