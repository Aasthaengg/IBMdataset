n = int(input())
t, a = map(int, input().split())
H = list(map(int, input().split()))
X = [abs(a - (t - h * 0.006)) for h in H]
print(X.index(min(X)) + 1)