N = int(input())
A = list(map(int, input().split()))
r = 0
while True:
    f = False
    for i, a in enumerate(A):
        if a%2 != 0:
            f = True
        A[i] = a//2
    if f: break
    r += 1
print(r)
