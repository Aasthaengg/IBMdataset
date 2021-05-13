N = int(input())
seat = [0]*100000
for i in range(N):
    a,b = map(int,list(input().split()))
    for j in range(a,b+1):
        seat[j-1] = 1
print(sum(seat))
