n = int(input())
a = list(map(int, input().split()))
def f():
    for i in range(100):
        for j in range(n):
            if a[j]%2 == 0:
                a[j] = a[j]//2
            else:
                return i
print(f())