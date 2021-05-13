import collections
n=int(input())
A=list(map(int,input().split()))
print(len(collections.Counter(A))-(n-len(collections.Counter(A)))%2)