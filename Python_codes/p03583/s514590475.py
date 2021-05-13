N = int(input())

for h in range(1, 3501):
    for n in range(1, 3501):
        temp1 = N * n * h
        temp2 = 4 * h * n - N * (n + h)
        if temp2 != 0:
            w = temp1 // temp2
            if w * temp2 == temp1 and w >= 1:
                ans = (h, n, w)
                break
h, n, w = ans
print(h, n ,w)