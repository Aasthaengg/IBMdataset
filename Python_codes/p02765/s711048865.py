import sys
input = sys.stdin.readline

N,R = list(map(int,input().split()))

if N >= 10:
    print(R)
else:
    print(R+100*(10-N))