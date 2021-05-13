N = int(input())

a = 0
b = 0

for i in range(1,10):
    if N > 100:
        N = N - 100
        a = a + 1

for j in range(1,10):
    if N > 10:
        N = N - 10
        b = b + 1
c = N

if a == c:
    print("Yes")
else:
    print("No")