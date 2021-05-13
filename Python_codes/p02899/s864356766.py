N = int(input())
A = list(map(int, input().split()))

B = [(i+1, k) for i, k in enumerate(A)]


def func(x):
    return x[1]


B.sort(key=func)
res = ""
for b in B:
    res += str(b[0]) + " "

print(res)