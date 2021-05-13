N = int(input())
A, B = [], []
for i in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

AB = sorted([s+t for s,t in zip(A,B)], reverse=True)
su = sum(AB[::2])
print(su-sum(B))