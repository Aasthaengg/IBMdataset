import sys
read=sys.stdin.read
readline=sys.stdin.readline

n=int(readline().strip())
k=int(readline().strip())
x=list(map(int,readline().split()))

print(sum([2*min(b,k-b) for b in x]))
