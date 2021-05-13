N = int(input())
A= list(map(int, input().split()))
temp = 1
for i in A:
    if i==temp:
        temp+=1
if temp==1:
    print(-1)
else:
    print(N-temp+1)