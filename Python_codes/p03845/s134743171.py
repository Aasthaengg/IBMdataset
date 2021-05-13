import sys
input = sys.stdin.readline

n = int(input())
t=list(map(int,input().split()))
sumt = sum(t)
for i in range(int(input())):
    p,x = list(map(int,input().split()))
    print(sumt+x -t[p-1])
