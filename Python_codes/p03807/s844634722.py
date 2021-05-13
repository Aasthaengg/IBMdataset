N = int(input())
*A, = map(int, input().split())

count = 0

for i in range(len(A)):
    if A[i]%2!=0:
        count = count + 1

if count%2==0:
    print("YES")
else:
    print("NO")