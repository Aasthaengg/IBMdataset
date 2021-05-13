n  = int(input())

d = {}
for _ in range(n):
    string = "".join(sorted(list(input())))
    if string not in d:
        d[string] = 1
    else:
        d[string] += 1

ans = 0
for v in d.values():
    ans += v*(v-1)//2

print(ans)


