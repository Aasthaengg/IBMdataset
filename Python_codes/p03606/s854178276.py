N = int(input())
count = 0
for i in range(N):
    a,b = map(int,input().split())
    count += b-a+1
print(count)