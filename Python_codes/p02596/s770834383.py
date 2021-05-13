K = int(input())

k = 1
a = 7
for i in range(10**6+5):
    if a%K == 0:
        print(k)
        exit()
    a = (a*10 + 7) % K
    k += 1
    
print(-1)