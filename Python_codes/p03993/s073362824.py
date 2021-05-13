N = int(input())
a = list(map(int,input().split()))

cnt = 0
for i,value in enumerate(a):
    b = a[value-1]
    if b == i+1:
        cnt += 1
cnt //=2
print(cnt)