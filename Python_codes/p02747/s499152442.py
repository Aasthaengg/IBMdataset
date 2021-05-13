import sys
input = sys.stdin.readline
"""
N,X=map(int,input().split())
vA=list(map(int,input().split()))
vA.sort()
"""

S=input().rstrip()
T="hi"

res=any(S==T*i for i in range(1,6))
print("No Yes".split()[res])
#print(res)
