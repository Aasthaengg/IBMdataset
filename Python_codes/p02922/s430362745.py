A, B = map(int, input().split())
for i in range(0, 20):
    if B <= A*i - (i - 1):
        print(i)
        break