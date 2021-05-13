nim = int(input())
array = [0] * 55556
prime = []
for i in range(2, 55556):
    if array[i] == 0:
        if i % 10 == 1:
            prime.append(i)
        for j in range(i, 55556, i):
            array[j] = 1
    if len(prime) == nim:
        print (*prime)
        exit()