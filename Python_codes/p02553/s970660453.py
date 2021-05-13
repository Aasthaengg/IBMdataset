import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
a,b,c,d=get_ints()
pro=[a*c,a*d,b*c,b*d]
print(max(pro))
