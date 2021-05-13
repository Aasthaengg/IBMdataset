n = int(input())
p = list(map(int, input().split()))
q = sorted(p)
diff = []
for i in range(n):
    if p[i] != q[i]:
        diff.append(i)
print("YES" if len(diff) <= 2 else "NO")