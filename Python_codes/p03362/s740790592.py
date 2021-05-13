n = int(input())
a = 11
p = [11]

def is_prime(x):
    if x%2==0:
        return False
        
    for i in range(3, x//2+1, 2):
        if x % i == 0:
            return False
    else:
        return True

while len(p) < n:
    a += 5
    if is_prime(a):
        p.append(a)

print(*p)
