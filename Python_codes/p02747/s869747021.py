import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    if len(s)%2==0:
        if s=='hi'*(len(s)//2):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
resolve()