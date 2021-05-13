import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    if s in ['hi','hihi','hihihi','hihihihi','hihihihihi']:
            print('Yes')
    else:
            print('No')
resolve()