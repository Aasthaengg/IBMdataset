x = list(input().split(" "))
c = int(x[2])
divisors = 0
for i in range(int(x[0]), int(x[1])+1):
    if c % i == 0:
        divisors += 1
print(divisors)