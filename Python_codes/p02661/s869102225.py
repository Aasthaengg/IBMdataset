import sys
import  math
import fractions
from collections import defaultdict
stdin = sys.stdin
     
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))


N=int(input())
min_l=[]
max_l=[]
for k in range(N):
    A,B=nm()
    min_l.append(A)
    max_l.append(B)

min_l.sort()
max_l.sort()

if(N%2==0):
    print(int(((max_l[N//2-1]+max_l[N//2])/2-(min_l[N//2-1]+min_l[N//2])/2)*2+1))    
else:
    print(((max_l[(N-1)//2])-(min_l[(N-1)//2]))+1)