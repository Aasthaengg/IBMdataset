import sys
import  math
import fractions
from collections import defaultdict
stdin = sys.stdin
     
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))
 
X=int(input())
ans=0
if(400<=X and X<=599):
    ans=8
if(600<=X and X<=799):
    ans=7
if(800<=X and X<=999):
    ans=6
if(1000<=X and X<=1199):
    ans=5
if(1200<=X and X<=1399):
    ans=4
if(1400<=X and X<=1599):
    ans=3
if(1600<=X and X<=1799):
    ans=2
if(1800<=X and X<=1999):
    ans=1
 
print(ans)