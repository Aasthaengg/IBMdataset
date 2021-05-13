k = int(input())
A = list(map(int, input().split()))
if A[-1] != 2:
    print(-1)
    exit()
L = 1
R = 2
for a in reversed(A):
    c = R//a-L//a
    if c == 0:
        print(-1)
        exit()
    L = (L//a+1)*a-1
    R = (R//a+1)*a-1
print(L+1, R)
