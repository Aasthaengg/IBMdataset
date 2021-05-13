N = int(input())
S = len(set(map(int, input().split())))
print(S - (N - S) % 2)
