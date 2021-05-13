I = int(input())
L = list(map(int, input().split()))

a = 0
b = 0
while len(L):
    a += L.pop(L.index(max(L)))
    if len(L) == 0: break;
    b += L.pop(L.index(max(L)))

print(abs(a-b))
