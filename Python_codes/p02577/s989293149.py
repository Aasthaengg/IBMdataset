#9の倍数
n = input()
s = list(n)
ss = [int(i) for i in s]
if sum(ss)%9==0:
    print("Yes")
else:
    print("No")


