n = int(input())
k = int(input())

num = 1

def ope_a(num_local):
    num_local = 2 * num_local
    return num_local

def ope_b(x):
    x = x + k
    return x

i = 0
while i < n:
    if ope_a(num) <= ope_b(num):
        num = ope_a(num)
        i += 1
    else:
        num = ope_b(num)
        i += 1

print(num)