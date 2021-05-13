n = int(input())
c = 0

def devisor(n):
    if n == 2:
        return 1
    else:
        if n < 2 or n % 2 == 0:
            return 0
        elif pow(2,n-1,n) == 1:
            return 1
        else: return 0

for i in range(n):
    x = int(input())
    c += devisor(x)

print(c)