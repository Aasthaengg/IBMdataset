import sys
n=int(input())
a=[int(i) for i in sys.stdin.readline().split()]
m=0
sums=0
for i in a:
    m=max(m,i)
    if i<m:
        sums+=m-i
    
print(sums)