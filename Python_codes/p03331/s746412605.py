N = int(input())

if (N%10 == 0):
    print(10)
    exit()
a = []
while N > 0:
    a.append(N%10)
    N //= 10

print(sum(a))
