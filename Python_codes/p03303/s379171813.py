import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    w=int(input())
    l=[]
    for i in range(-(-len(s) // w)):
        l.append(s[w*i])
    print(''.join(l))
resolve()