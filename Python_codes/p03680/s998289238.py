n = int(input())
a = [int(input()) for i in range(n)]

flag = True
position = 1

for i in range(n):
    position = a[position-1]
    if position == 2:
        print(i+1)
        flag = False
        break
        
if flag:
    print(-1)