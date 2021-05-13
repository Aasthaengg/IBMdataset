D, N = map(int, input().split())
S = list(map(int, input().split()))
print(D-sum(S) if D >= sum(S) else '-1')