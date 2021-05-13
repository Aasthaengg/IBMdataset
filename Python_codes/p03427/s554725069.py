import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=input()
    keta=len(n)
    saileft=int(n[0])
    if n[1:].count('9')==keta-1:
        print(saileft+(keta-1)*9)
    else:
        print(saileft-1+9*(keta-1))
resolve()
