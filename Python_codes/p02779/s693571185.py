import collections

N=int(input())
A=list(map(int,input().split()))
a=collections.Counter(A).most_common()
print("YES" if a[0][1]==1 else "NO")
