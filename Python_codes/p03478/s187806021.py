n_a_b = input().split(' ')

n = int(n_a_b[0])
sum([int(i) for i in list(n_a_b[0])])
a = int(n_a_b[1])
b = int(n_a_b[2])

result = 0
for i in range(1, n+1):
    total = sum([int(s) for s in list(str(i))])
    if total >= a and total <= b:
        result += i

print(result)