N = int(input())
if N%2:
    print(0)
else:
    a = 0
    for i in range(1, 40):
        a += N//2//5**i
    print(a)
