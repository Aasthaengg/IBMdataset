n,m = map(int, input().split())
A = list(map(int, input().split()))
x = sum(A)*1/(4*m)
A = [i for i in A if i>=x]
print("Yes" if len(A)>=m else "No")