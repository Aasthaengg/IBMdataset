n = int(input())
p = [int(i) for i in input().split()]
sp = sorted(p)
print('YES' if sum(p[i] == sp[i] for i in range(n)) >= n - 2 else 'NO')