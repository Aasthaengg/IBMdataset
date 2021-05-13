n = int(input())
a = list(map(int,input().split()))

flag = False
doit = 0
while flag == False:
    counter = 0
    for x in a:
        if x % 2 == 1:
            flag = True
        else:
            a[counter] = x / 2
            counter += 1
    doit += 1
print(doit - 1)