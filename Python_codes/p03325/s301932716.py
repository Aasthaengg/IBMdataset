N=int(input())
a=list(map(int,input().split()))

S=0
for i in range(N):
    cnt=0
    while a[i] % 2 == 0:
        a[i]//= 2
        cnt += 1
    S+=cnt
print(S)