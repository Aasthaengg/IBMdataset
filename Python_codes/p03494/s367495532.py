N = int(input())
A = list(map(int, input().split()))
tf = True
cnt = 0
while tf == True:
    for i in range(N):
        if A[i] % 2 != 0:
            tf = False
    if tf == True:
        cnt += 1
        for i in range(N):
            A[i] //= 2
print(cnt)
