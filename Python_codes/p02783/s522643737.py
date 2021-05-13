import sys,math
input = sys.stdin.readline

H,A=list(map(int,input().split()))
print(math.ceil(H/A))
