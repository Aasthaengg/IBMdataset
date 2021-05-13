s = input()
n = int(s)

count = 0
divisors = 0

arrays = []
for i in range(n+1):
    arrays.append(False)

for i in range(n+1):
    if i % 2 == 1:
        divisors = 0
        for j in range(len(arrays)):
            arrays[j] = False
        for j in range(1,i+1):
             if i % j == 0:
                 arrays[j] = True
        for j in range(len(arrays)):
            if arrays[j]:
                divisors += 1
        if divisors == 8:
            count += 1

print(count)