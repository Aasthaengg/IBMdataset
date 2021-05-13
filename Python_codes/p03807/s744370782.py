n = int(input())
a = list(map(int, input().split()))
if sum([1 for b in a if b%2 == 1]) % 2 == 1:
    print('NO')
else:
    print('YES')