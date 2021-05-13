h,w = map(int, input().split())
l = []
for i in range(h):
    l.extend(input())
import collections
c = collections.Counter(l)
num4=(h//2) * (w//2)
if h%2!=0 and w%2!=0:
    num1=1
else:
    num1=0
num2 = ((h*w) - (4*num4 + num1))//2
cnts = list(c.values())

for i in range(num4):
    for j in range(len(cnts)):
        if cnts[j] >= 4:
            cnts[j] -= 4
            break
    else: # not broken -> error
        print("No")
        exit()

for i in range(num2):
    for j in range(len(cnts)):
        if cnts[j] >= 2:
            cnts[j] -= 2
            break
    else: # not broken -> error
        print("No")
        exit()

for i in range(num1):
    for j in range(len(cnts)):
        if cnts[j] >= 1:
            cnts[j] -= 1
            break
    else: # not broken -> error
        print("No")
        exit()

print("Yes")