a, b, N = list(map(int, input().split()))

divisors_list = []
for i in range(a,b+1):
    divisor = N%i
    if divisor == 0:
        divisors_list.append(divisor)

print(len(divisors_list))