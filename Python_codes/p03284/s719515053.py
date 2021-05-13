N,K=map(int,input().split())
if N<K:
    print("1")
elif N%K>=2 and N>K:
    print("1")
else:
    print(N%K)