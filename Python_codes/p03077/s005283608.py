n = int(input())
ls = [int(input()) for _ in range(5)]
k = n//min(ls)
if (n/min(ls)) % 1 != 0:
    k += 1
print(k+4)
