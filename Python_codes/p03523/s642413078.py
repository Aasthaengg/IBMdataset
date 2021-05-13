import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    import re
    s=input()
    ans=re.fullmatch(pattern=r'A?KIHA?BA?RA?',string=s)
    print('YES' if ans else 'NO')
resolve()