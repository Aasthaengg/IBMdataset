n = int(input())
li = list(map(int,input().split()))
x = 0
y = 0

for i in li:
    if i%4 == 0: #4の倍数がカバーできるのはx*2+1個まで
        x += 1
    if i%4 != 0 and i%2 == 0: #4の倍数では無いけど2の倍数がカバーできるのは自分たちのみ
        y += 1

if x>0 and y>0:
    if 2*x+y >= n:
        print("Yes")
    else:
        print("No")

elif x>0:
    if 2*x+1 >= n:
        print("Yes")
    else:
        print("No")

elif y>0:
    if y == n:
        print("Yes")
    else:
        print("No")

else:
    print("No")