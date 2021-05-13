#C
N=int(input())
X=list(map(int,input().split()))

P=round(sum(X)/N,0)
vital_sum=0
for i in X:
    vital_sum+=(i-P)**2
print(int(vital_sum))