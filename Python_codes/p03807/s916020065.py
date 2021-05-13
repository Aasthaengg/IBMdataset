n = int(input())
A = list(map(int, input().split()))
EO = [i % 2 for i in A]
print('YES' if EO.count(1) % 2 == 0 else 'NO')