N,A,B = list(map(lambda x: int(x),input().split()))
X = list(map(lambda x: int(x),input().split()))
total=0
for i in range(N-1):
    d = X[i+1]-X[i]
    total += min(d*A,B)
print(total)
