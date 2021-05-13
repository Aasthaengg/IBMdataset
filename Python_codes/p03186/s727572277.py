A,B,C = map(int, input().split())

if A + 1 >= C:
    print(B + C)
    exit()
else:
    ans = A
    C -= A

if B + 1 >= C:
    print(ans + B + C)
else:
    print(ans + B + (B + 1))