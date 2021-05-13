n, k = list(map(int, input().split()))
kl = [[] for _ in range(k)]
for i in range(k):
    a = int(input())
    d = list(map(int, input().split()))
    kl[i].append(d)
f1 = set(sum(sum(kl, []), []))
r = set(i for i in range(1, n + 1))
print(len(r - f1))
