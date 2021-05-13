import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
cnt = sum(b) - sum(a)
diff1 = [] # a > b
diff2 = [] # b > a
for i, j in zip(a, b):
    if i > j:
        diff1.append(i - j)
    elif j > i:
        diff2.append(j - i)

if cnt < sum(diff1):
    print("No")
    sys.exit()
else:
    cnt -= sum(diff1)

a_add = cnt + sum(diff1) # 2を足す
b_add = cnt # 1を足す

c = []
for i in diff2:
    if i % 2 == 0:
        a_add -= i//2
    else:
        c.append(1)
        a_add -= (i - 1)//2
a_add -= sum(c)
b_add -= sum(c)
if a_add*2 == b_add and a_add >= 0 and b_add >= 0:
    print("Yes")
else:
    print("No")