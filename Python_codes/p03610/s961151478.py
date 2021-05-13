import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    print(s[::2])
resolve()