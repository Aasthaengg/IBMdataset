N = int(input())
A = list(map(int,input().split()))
count,okey=0,0

for i in range(N):
    if A[i]%2 == 0:
        count += 1
        if A[i]%3==0 or A[i]%5==0:
            okey += 1

if count==okey:
    print("APPROVED")
else:
    print("DENIED")