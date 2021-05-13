n = int(input())
count = [0] * n
for i in range(n) :
    for j in range(6, -1, -1) :
        if (i+1) % 2**j == 0 :
            count[i] = j
            break
max = max(count)
print(count.index(max)+1)
