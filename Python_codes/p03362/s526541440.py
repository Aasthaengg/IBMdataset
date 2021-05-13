
n = int(input())
j = 0
data = [0] * n
i = 2
while j < n:
    divcnt = 0
    for k in range(1, i * 5 + 2):
        if (i * 5 + 1) % k == 0:
            divcnt += 1
        
    if divcnt == 2:
        data[j] = i * 5 + 1
        j += 1
    
    i += 1
    
for i in range(n):
    print("{0} ".format(data[i]), end = "")
