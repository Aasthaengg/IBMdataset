n = int(input())
a = [int(i) for i in input().split()]
def div2(m):
    i = 0
    while m % 2 == 0:
        m = m // 2
        i += 1
    return i
total = 0
for j in a:
    total += div2(j)
print(total)