N = int(input())
A,B = map(int,input().split())
P = list(map(int,input().split()))
P.sort()
count1,count2,count3 = 0,0,0
for i in range(N):
  if P[i] <= A:
    count1 += 1
  if P[i] >= B+1:
    count3 += 1
    continue
  if P[i] >= A+1:
    count2 += 1
print(min(count1,count2,count3))