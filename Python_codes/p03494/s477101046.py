N = int(input())
a = list(map(int,input().split()))
count=0
while True:
    flag = False
    for i in range(N):
        if a[i] % 2==1:
            flag = True
    if flag:
        break
    for i in range(N):
        a[i]/=2

    count += 1

print(count)