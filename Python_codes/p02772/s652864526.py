n = int(input())
a = list(map(int, input().split()))
print('DENIED' if sum(ai % 3 and ai % 5 for ai in a if ai % 2 == 0) else 'APPROVED')