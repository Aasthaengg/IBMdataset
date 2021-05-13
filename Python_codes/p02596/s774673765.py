K = int(input())

x = 7%K

for i in range(K):
    if x == 0:
        print(i+1)
        exit()
    x = (x*10+7)%K
print(-1)
