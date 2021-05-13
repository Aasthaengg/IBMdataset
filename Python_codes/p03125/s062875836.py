A, B = map(int, input().split())
for i in range(B+1):
    if i == 0:
        continue
    if B % (A*i) == 0:
        print(A + B)
        exit()
print(B - A)