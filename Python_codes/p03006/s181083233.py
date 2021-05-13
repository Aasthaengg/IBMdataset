from collections import Counter
n=int(input())
A=[list(map(int,input().split())) for i in range(n)]
Per=[(a[0]-b[0],a[1]-b[1]) for a in A for b in A if a!=b]
print(n-Counter(Per).most_common(1)[0][1] if n!=1 else 1)