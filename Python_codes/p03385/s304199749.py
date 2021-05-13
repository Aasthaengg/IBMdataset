import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    if set(input())=={'a','b','c'}:
        print('Yes')
    else:
        print('No')
resolve()