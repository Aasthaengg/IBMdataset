from sys import stdin
n = int(stdin.readline().rstrip())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
li = make_divisors(n)
point = 0
for i in li:
    minashi = i-1
    if minashi == 0:
        continue
    elif n%minashi == n//minashi:
        point += minashi
print(point)