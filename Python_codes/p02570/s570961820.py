from sys import stdin

input = stdin.readline

D, T, S = map(int, input().split())
print('Yes' if S*T >= D else 'No')