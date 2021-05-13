n = int(input())
p = list(map(int, input().split()))
print('YES' if sum(p[i] != i + 1 for i in range(n)) <= 2 else 'NO')