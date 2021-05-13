import sys
input = sys.stdin.readline

N=int(input())
flag = 0
for _ in range(N):
    if int(input())%2==1:
        flag = 1
print('first' if flag else 'second')
