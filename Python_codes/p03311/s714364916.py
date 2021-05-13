import statistics
N = int(input())
A = list(map(int,input().split()))
A2 = sorted([A[i]-i-1 for i in range(N)])
med = int(statistics.median(A2))
med2 = med+1
sum1 = 0
sum2 = 0
for i in range(N):
    sum1 += abs(A2[i]-med)
    sum2 += abs(A2[i]-med2)
print(min(sum1,sum2))