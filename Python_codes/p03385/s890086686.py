import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    if s in ['abc','acb','bca','bac','cab','cba']:
        print('Yes')
    else:
        print('No')
resolve()