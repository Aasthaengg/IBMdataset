N=int(input())
H=list(map(int,input().split()))
max = 0
n = 0
for i in range(1,N):
    if H[i] <= H[i-1]:
        n += 1
        if n > max:
            max = n
    else:
        n = 0

print(max)

