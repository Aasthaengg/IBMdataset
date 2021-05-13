from sys import stdin
input = stdin.readline

a = input().strip()
res = sum(int(i) for i in a) % 9 == 0
print('Yes' if res else 'No')