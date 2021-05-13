n = int(input())
h = list(map(int, input().split()))

flag = True

x = h[0] - 1

for i in range(1, n):
    if h[i] < x:
        flag = False
        break
    elif h[i] == x:
        pass
    else:
        x = h[i] - 1
    
if flag:
    print("Yes")
else:
    print("No")