a, b, c = map(int, input().split())
k = int(input())
L = sorted([a, b, c])
print(L[0] + L[1] + L[2]*2**k)