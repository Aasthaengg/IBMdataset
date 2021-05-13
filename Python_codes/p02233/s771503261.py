n = int(input())

def fb(num):
    a, b = 1, 0
    for i in range(num):
        a, b = a + b, a
    return b

print(fb(n+1))
