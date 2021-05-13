cntr = 0
n = int(input())
S = input()
for s in S:
    if s == "R":cntr+=1
if cntr * 2 > n:
    print("Yes")
else:
    print("No")    