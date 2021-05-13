def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

X = int(input())
lis = [i for i in range(1,34)]
num = []

for i in lis:
    for j in range(2, 11):
        if i**j <= X:
            num.append(i**j)

print(max(num))