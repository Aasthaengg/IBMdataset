
import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    if 'C' in s and 'F' in s and s.find('C')<s.rfind('F'):
        print('Yes')
    else:
        print('No')
resolve()