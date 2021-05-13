n = int(input())
ls = list(map(int,input().split()))
di = [0]*n
di[0] = sum(ls)//2 - sum(ls[1::2])
for i in range(1,n):
    di[i] = ls[i-1] - di[i-1]
di = list(map(lambda x:2*x,di))
print(*di)