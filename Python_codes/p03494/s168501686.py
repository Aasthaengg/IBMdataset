n = int(input())
li = list(map(int,input().split()))

count = 0
flag = False
while True:
    for i in range(n):
        if li[i]%2==1:
            flag = True
        li[i]/=2
    if flag:
        break
    count+=1

print(count)
