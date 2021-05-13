N = int(input())
number = [0]*N
for i in range(N):
    a,b = map(int,input().split())
    if a==b:
        number[i]=1

for i in range(N-2):
    if number[i]==1 and number[i+1]==1 and number[i+2]==1:
        print("Yes")
        exit(0)

print("No")
