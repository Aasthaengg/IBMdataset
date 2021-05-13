N = int(input())

L = [i for i in map(int, input().split())]

m = max(L)

d = sum(L)-m

print("Yes" if d > m else "No")
