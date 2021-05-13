n = int(input())
a = list(map(int, input().split()))

l = [a[i] % 2 for i in range(n)]
print('YES' if l.count(1) % 2 == 0 else 'NO')