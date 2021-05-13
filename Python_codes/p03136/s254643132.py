N = int(input())
L = list(map(int,input().split()))

L.sort()
print("Yes" if L[N-1]<sum(L[0:N-1]) else "No")
