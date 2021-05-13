n = int(input())
i = 0
while True:
    t = 1000*i
    if t >= n:
        p = t - n
        break
    i +=1
print(p)