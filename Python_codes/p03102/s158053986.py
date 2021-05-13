from sys import stdin

n,m,c = map(int, input().split())
B = list(map(int, input().split()))
ALines = stdin.readlines()

print(sum([1 for A in ALines if sum([a*b for a,b in zip(list(map(int, A.split())),B)]) + c > 0]))