n = int(input())
approved = all([i % 2 != 0 or i % 10 == 0 or i % 6 == 0 for i in map(int, input().split())])
print('APPROVED' if approved  else 'DENIED')