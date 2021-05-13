A, B, K = map(int, input().split())
def h(x):
    if x%2==0:
        return int(x/2)
    else:
        return int((x-1)/2)
for i in range(K):
    if i%2 == 0:
        A = h(A)
        B = B + A
    else:
        B = h(B)
        A = A + B
print(A, B)
