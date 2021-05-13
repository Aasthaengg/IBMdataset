n = int(input())
al = list(input())
bl = list(input())
cl = list(input())

ans = 0
for a, b, c in zip(al, bl, cl):
    ans += len(set([a, b, c])) - 1
print(ans)