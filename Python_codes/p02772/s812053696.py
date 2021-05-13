N = input()
ints = (i for i in map(int, input().split()) if i % 2 == 0)
ints = (i % 3 == 0 or i % 5 == 0 for i in ints)
print('APPROVED' if all(ints) else 'DENIED')