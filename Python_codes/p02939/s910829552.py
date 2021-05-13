from sys import stdin
def S(): return stdin.readline().rstrip()

s = S()
ls = list(s)
l = []

tmp = ''
k = 0
for i in ls:
    k += 1
    if len(l)<1:
        l.append(i)
    else:
        tmp += i
        if tmp != l[len(l)-1]:
            l.append(tmp)
            tmp = ''
        else:
            if k == len(ls):
                a = l.pop()
                tmp = a+tmp
                l.append(tmp)

print(len(l))