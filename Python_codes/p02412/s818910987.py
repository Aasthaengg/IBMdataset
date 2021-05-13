count_a = []
pos = 0
while True:
    n, x = list(map(int, input().split()))
    count = 0
    if n == x == 0:
        break
    else:
        for i in range(1, (n+1)):
            for j in range(i+1, (n+1)):
                for k in range(j+1, (n+1)):
                    if (i != j) and (j != k) and (i != k):
                        if (i+j+k) == x:
                            count += 1
        count_a.append(count)
        pos = pos+1

for i  in count_a:
    print(i)
