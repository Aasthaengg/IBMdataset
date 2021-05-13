N = int(input())
A = list(map(int, input().split()))
print('YES' if len([i for i in A if i % 2 == 1]) % 2 == 0 else 'NO')