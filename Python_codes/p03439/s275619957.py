import sys
flush = sys.stdout.flush

d = {"M":0, "F":1}
def check(i):
    print(i)
    flush()
    s = input()
    if s[0] == "V":
        exit()
    return d[s[0]]

n = int(input())
left = 0
right = n-1
ls = check(left)
rs = check(right)

while right-left > 1:
    mid = (right+left)//2
    c = check(mid)
    if (c+mid-left)%2 == ls:
        left = mid
        ls = c
    else:
        right = mid