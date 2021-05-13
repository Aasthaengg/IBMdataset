n = int(input())
L = list(map(int,input().split()))

cnt = 0
ud = 0
ch = 1
for i in range(n-1):
    if L[i] < L[i+1] and ud == -1 and ch == 0:
        ch = 1
        ud = 1
        cnt +=1
    elif L[i] < L[i+1] and ch ==1:
        ch = 0
        ud = 1
    elif L[i] > L[i+1] and ud == 1 and ch == 0:
        ch = 1
        ud= -1
        cnt +=1
    elif L[i] > L[i+1] and ch == 1:
        ch = 0
        ud = -1
print(cnt+1)