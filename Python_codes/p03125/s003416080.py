A,B = map(int, input().split())
b = []
for i in range(1,21):
    if B % i == 0:
        b.append(i)
if A in b:
    print(A+B)
else:
    print(B-A)