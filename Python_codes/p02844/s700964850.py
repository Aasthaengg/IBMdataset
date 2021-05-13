n=int(input())
s=input()

lst = [0]*1000
sm = 0
first = [False]*10
second = [False]*100
for i in s:
    i = int(i)
    for j in range(100):
        if not second[j]:
            continue
        tmp = 10*j + i
        if lst[tmp] == 0:
            sm +=1
            lst[tmp]+=1

    for j in range(10):
        if first[j]:
            tmp = 10*j + i
            if not second[tmp]:
                second[tmp] = True

    if not first[i]:
        first[i] = True

print(sm)
