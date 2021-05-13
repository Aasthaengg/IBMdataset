import sys
import collections

def swap(t):
    if t[1] < t[0] :
        return (t[1],t[0])
    else:
        return t

n = int(sys.stdin.readline().rstrip())
a = [int(x) for x in sys.stdin.readline().rstrip().split()]

zippeda = list(map(swap,list(zip(range(1,n+1),a))))
zippeda.sort()
c = collections.Counter(zippeda)
counter = 0
for a in c.most_common():
    if a[1] < 2:
        break
    else:
        counter = counter + 1

print(counter)
