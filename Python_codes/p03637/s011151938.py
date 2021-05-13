n = int(input())
ls = list(map(int,input().split()))
j = 0
k = 0
p = 0
for i in range(n):
    if ls[i] % 4 == 0:
        j += 1
    elif ls[i] % 2 == 0:
        k += 1
if len(ls) % 2 == 0:
    if j >= len(ls)/2:
        print("Yes")
    else:
        p = (len(ls)/2 - j) * 2
        if k >= p:
            print("Yes")
        else:
            print("No")
else:
    if j >= int(len(ls)/2):
        print("Yes")
    else:
        p = (int(len(ls)/2) - j) * 2 +1
        if k >= p:
            print("Yes")
        else:
            print("No")