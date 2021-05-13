A = [[1,3,5,7,8,10,12],[4,6,9,11],[2]]
x,y = map(int, input().split())
flg = 0
for a in A:
    if x in a and y in a:
        flg = 1

if flg == 1:
    print("Yes")
else:
    print("No")