N = int(input())
D,X = map(int,input().split())
kosuu = X
for i in range(N):
    kosuu += (D-1)//int(input()) + 1
print(kosuu)