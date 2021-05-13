X=int(input())
max = 1
for i in range(2,33):
    k = 2
    while True:
        n = i**k
        if n > X:
            break
        if n > max:
            max = n
        k += 1
print(max)
