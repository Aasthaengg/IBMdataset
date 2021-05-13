from sys import stdin
def ip(): return [int(i) for i in stdin.readline().split()]
def sp(): return [str(i) for i in stdin.readline().split()]


d,t,s = ip()
if (d/s) > t: print("No")
else: print("Yes")