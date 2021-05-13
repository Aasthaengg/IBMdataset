k,t = map(int, input().split())
A = list(map(int,input().split()))

maxnum = max(A)
print(max(0, maxnum-1-(k-maxnum)))
