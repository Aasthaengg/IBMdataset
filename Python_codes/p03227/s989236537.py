import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    if len(s)==2:
        print(s)
    else:
        print(s[2]+s[1]+s[0])
resolve()
