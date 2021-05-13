import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    a=s.find('C')
    b=s.rfind('F')
    if a==-1 or b==-1:
        print('No')
    else:
        if a<b:
            print('Yes')
        else:
            print('No')
resolve()