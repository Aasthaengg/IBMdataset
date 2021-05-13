import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

n = I()
a = LI()

# a[0] の符号を決めて貪欲に

# a[0] > 0 にする

s = 0  # 累積和
b = 0  # 操作回数
for i in range(n):
    if i % 2 == 0:
        if s+a[i] > 0:
            s += a[i]
        else:
            b += -(s+a[i])+1
            s = 1
    else:
        if s+a[i] < 0:
            s += a[i]
        else:
            b += s+a[i]+1
            s = -1

# a[i] < 0 にする

s = 0  # 累積和
c = 0  # 操作回数
for i in range(n):
    if i % 2 == 1:
        if s+a[i] > 0:
            s += a[i]
        else:
            c += -(s+a[i])+1
            s = 1
    else:
        if s+a[i] < 0:
            s += a[i]
        else:
            c += s+a[i]+1
            s = -1

print(min(b,c))
