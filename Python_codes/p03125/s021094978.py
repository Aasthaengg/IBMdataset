import sys
input = sys.stdin.readline

N, M = map(int,input().split())
if M%N==0:
    print(M+N)
else:
    print(M-N)