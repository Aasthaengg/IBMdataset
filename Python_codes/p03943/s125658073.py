import sys
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

l=sorted(lmp())
if l[0]+l[1]==l[2]:
    print("Yes")
else:
    print("No")