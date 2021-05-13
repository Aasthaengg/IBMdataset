import sys
sys.setrecursionlimit(10**6)

#a = int(input())
#b = list(map(int, input().split()))
#n, m = map(int, input().split())
s = input()
#s,t = input().split()
#a = [int(input()) for _ in range(n)]
#
#readline = sys.stdin.readline
#n,m = [int(i) for i in readline().split()]
#ab = [[int(i) for i in readline().split()] for _ in range(n)]

l = [i for i in range(1,13)]
l = [str(i) if len(str(i))==2 else '0'+str(i) for i in l]

if s[:2] not in l and s[2:] not in l:
    print('NA')
elif s[:2] not in l and s[2:] in l:
    print('YYMM')
elif s[:2] in l and s[2:] not in l:
    print('MMYY')
else:
    print('AMBIGUOUS')