N = int(input())
A = list(map(int, input().split()))

mt_rain =[0]*N
mt_all =sum(A)
dam_even = sum(A[1::2]) #偶数番目のダムの増えた水
mt_rain[0] = mt_all - 2*dam_even #1番目の山の降水量

#2番目の山以降
for i in range(1,N):
    mt_rain[i] =2*A[i-1] -mt_rain[i-1]
print(*mt_rain)