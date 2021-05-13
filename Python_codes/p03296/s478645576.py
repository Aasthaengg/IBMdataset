n = int(input())
a = list(map(int,input().split()))
flg = 0
counter = 0
for i in range(n-1):
    if a[i] == a[i+1]:
        if flg == 0:
            counter +=1
            flg = 1
        else:
            flg = 0
    else:
        flg = 0
print(counter)       