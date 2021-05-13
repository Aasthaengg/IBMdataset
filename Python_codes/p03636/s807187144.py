import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    print(s[0]+str(len(s)-2)+s[-1])
resolve()