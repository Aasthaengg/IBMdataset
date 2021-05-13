n = 0
x = 0
cnt = 0

while True:
    
    I = input().split()
    n = int(I[0])
    x = int(I[1])
    if n == 0 and x == 0:
        break
    
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                if (i + j + k) == x:
                    cnt += 1
                    continue
    print(cnt)
    cnt = 0