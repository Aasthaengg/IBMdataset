N = int(input())
H = list(map(int, input().split()))

f = False #まだ下げられる->False / もう下げられない->True
for i in range(N-1, 0, -1):
    if H[i-1] - H[i] > 1:
        print("No")
        exit()
    elif H[i-1] - H[i] == 1 and not f:
        f = True
    elif H[i-1] - H[i] == 1 and f:
        print("No")
        exit()
    elif H[i-1] - H[i] == 0:
        pass
    elif H[i-1] - H[i] < 0:
        f = False
print("Yes")