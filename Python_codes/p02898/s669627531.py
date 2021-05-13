N, K = map(int,input().split())
h = list(map(int,input().split()))
Kijo = [i for i in h if i >= K]
print(len(Kijo))