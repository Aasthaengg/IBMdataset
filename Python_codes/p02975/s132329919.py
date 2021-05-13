import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())

if sum(As)==0:
    print('Yes')
elif N%3!=0:
    print('No')
else:
    from collections import Counter
    d = N//3
    c = Counter(As)
    if len(set(As))>3:
        print('No')
    elif len(set(As))==3:
        items = list(set(As))
        a = 0
        for item in items:
            a ^= item
            if not c[item]==d:
                print('No')
                break
        else:
            if a!=0:
                print('No')
            else:
                print('Yes')
    else:
        if c[0]==d:
            print('Yes')
        else:
            print('No')