import sys
input = sys.stdin.readline
n=int(input())
l=sorted(list(map(int,input().split())))
print('Yes' if sum(l[:-1])>l[-1] else 'No')