import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip() # input string
ni = lambda: int(readline().rstrip()) # input int
nm = lambda: map(int, readline().split()) # input multiple int 
nl = lambda: list(map(int, readline().split())) # input multiple int to list

n = ni()
a = nl()

sa = set(a)
l = len(sa)

if l == 1:
    if a[0] == 0:
        print('Yes')
    else:
        print('No')
elif len(a) % 3 == 0:
    if l == 2:
        if a.count(0) == n // 3:
            print('Yes')
        else:
            print('No')
    elif l == 3:
        if all([a.count(ele) == n // 3 for ele in sa]):
            li = list(sa)
            if li[0] ^ li[1] ^ li[2] == 0:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')
