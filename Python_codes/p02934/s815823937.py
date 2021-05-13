N = int(input())
S = list(map(int, input().split()))
S2 = list(map(lambda x: 1/x, S))
print(1/sum(S2))