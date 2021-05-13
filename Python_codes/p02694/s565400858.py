n = int(input())

num = 100
i = 0
while num <=n:
    num = num*101//100
    i +=1
    if num >= n:
        print(i)
        exit()