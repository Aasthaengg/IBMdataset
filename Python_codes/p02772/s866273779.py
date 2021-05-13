n = input()
a = map(int, input().split())
print('APPROVED' if all(ai % 2 == 1 or ai % 3 == 0 or ai % 5 == 0 for ai in a) else 'DENIED')
