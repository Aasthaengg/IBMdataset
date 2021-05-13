n,m = map(int,input().split())
Ai = list(map(int,input().split()))
print(n - sum(Ai) if n - sum(Ai) >= 0 else -1)