A, B, K = [int(i) for i in input().split()]
result_list = []

def divisor_list(n):
    i = 1
    array = []
    while i * i <= n:
        if n % i == 0:
            array.append(i)
            array.append(n//i)
        i += 1
    array = list(set(array))
    return array

for i in divisor_list(A):
    for j in divisor_list(B):
        if i == j:
            result_list.append(i)

print(sorted(result_list)[-K])