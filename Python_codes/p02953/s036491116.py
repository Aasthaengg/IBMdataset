n = int(input())
squeres = list(map(int, input().split()))
flag = True
before_down = 0
for i in range(n - 1):
    if squeres[i] > squeres[i + 1] and squeres[i] - 1 <= squeres[i + 1] and before_down == 0:
        before_down = 1

    elif not squeres[i] <= squeres[i + 1]:
        flag = False
    
    else:
        if squeres[i] < squeres[i + 1]:
            before_down = 0
if flag:
    print("Yes")
else:
    print("No")
