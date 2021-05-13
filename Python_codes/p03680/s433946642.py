N = int(input())
a = [int(input()) for i in range(N)]
count = [0]*N
i = 0

while(True):
    count[i]+=1
    i = a[i]-1
    if i == 1:
        print(sum(count))
        break
    if count[i] == 1:
        print(-1)
        break