from sys import stdin
input = stdin.readline

n,x,t = map(int,input().split())
print((n+x-1)//x*t)