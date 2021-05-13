N = int(input())
s = input().rstrip()

R = s.count('R')
B = s.count('B')
print('Yes' if R > B else 'No')
