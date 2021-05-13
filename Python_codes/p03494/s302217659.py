n = int(input())
num = [int(x) for x in input().split()]
count = 0
a = 0

while(a==0):
    nl = []
    sl = []
    for i in num:
        if i %2 ==0:
            nl.append(i/2)
        else:
            sl.append(i)
    if sl == []:
        num =nl
        count += 1
    else:
        a = 1

print(count)