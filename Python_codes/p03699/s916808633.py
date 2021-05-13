N = int(input())
chin = []
sum = 0

for i in range(N):

    x = int(input())
    sum += x

    if x % 10 != 0:
        chin.append(x)

chin.sort()
i = 0

while chin != [] and i < len(chin) and sum % 10 == 0:
    sum -= chin[i]
    i += 1

if sum % 10 == 0:
    print(0)
else:
    print(sum)
