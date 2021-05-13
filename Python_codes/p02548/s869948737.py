N = int(input())
 
N_1 = N - 1
counts = 0
i = 1
j = 1
while i <= N_1:
    while j <= N_1:
        if i * j <=  N_1:
            counts = counts + 1
        else:
            j = N_1
        j = j + 1
    j = 1
    i = i + 1
 
print(counts)