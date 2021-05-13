i9 = 10 ** 9
S = int(input())
if S == i9 ** 2:
    print(i9, 0, 0, i9, 0, 0)
else:
    print(i9 - (S % i9), S // i9 + 1, i9, 1, 0, 0)
