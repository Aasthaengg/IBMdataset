s = input()
t = input()

d = {}
use = set()
for si,ti in zip(s,t):
    if(si in d):
        if(ti != d[si]):
            print('No')
            exit()
    else:
        if(ti in use):
            print('No')
            exit()
        d[si] = ti
        use.add(ti)

print('Yes')