n = int(input())

total = 0

for i in range(1, int(n**0.5)+1):
    if n%i == 0:
        a = i
        b = n//i

        if a != 1 and (n//(a-1))*a == n:
            total += a-1
        if b != a and (n//(b-1))*b == n:
            total += b-1

print(total)