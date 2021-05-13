import sys
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

s=input()
l=[]
l.append(s.count("a"))
l.append(s.count("b"))
l.append(s.count("c"))

if max(l)-min(l)<=1:
    print("YES")
else:
    print("NO")