n,k=map(int,input().split())

myset = set()
for i in range(k):
    d=input()
    l=list(map(int,input().split()))
    myset |= set(l)

print(n-len(myset))