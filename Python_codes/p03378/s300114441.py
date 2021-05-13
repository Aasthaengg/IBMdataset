n, m, x = map(int, input().split())
a = list(map(int, input().split()))
r = [0 for _ in range(n+1)]
for i in a:
    r[i] += 1
print(min(sum(r[x:]), sum(r[:x+1])))