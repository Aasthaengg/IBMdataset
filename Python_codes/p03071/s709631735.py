A, B = map(int, input().split())
res = 0
for i in range(2):
    if A <= B:
        res = res + B
        B = B -1
    else:
        res = res + A
        A = A -1
print(res)