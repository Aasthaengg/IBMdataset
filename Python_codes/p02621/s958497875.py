N = 10**7

M = 10**5
arr = list(range(M))


def f(x):
    return x


for i in range(N):
    b = arr[i % M]
    b = f(b)

a = int(input())
print(a + a**2 + a**3)
