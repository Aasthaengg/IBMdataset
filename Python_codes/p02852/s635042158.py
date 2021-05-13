import sys
n, m = [int(i) for i in sys.stdin.readline().split()]
s = input()
ind = n
ls = []
while ind > 0:
    flg = False
    for i in range(min(m, ind), 0, -1):
        if s[ind - i] == "0":
            ind -= i
            flg = True
            break
    if not flg:
        ls = []
        i = -1
        ind = 0
    ls.append(str(i))
print(" ".join(ls[::-1]))