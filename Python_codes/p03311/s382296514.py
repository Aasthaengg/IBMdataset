N = int(input())
A = list(map(int,input().split()))
for i in range(N):
  A[i]-= i+1
A.sort()
total = sum(A)
mean1 = total//N
mean2 = total//N + 1
med1 = A[N//2]
#med2 = A[N//2+1]
ans1 = 0
ans2 = 0
ans3 = 0
ans4 = 0 
for a in A:
  ans1+=abs(a-mean1)
  ans2+=abs(a-mean2)
  ans3+=abs(a-med1)
  #ans4+=abs(a-med2)
print(min([ans1,ans2,ans3]))