N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]
chocolate = [i for j in A for i in range(1, D+1, j)]
print(len(chocolate)+X)