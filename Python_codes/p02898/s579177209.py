N,K=list(map(int, input().split()))
H=list(map(int, input().split()))
print(len([h for h in H if h >= K]))