N = int(input())
p = list(map(int,input().split()))
count = 0
for i in range(N-2):
    if p[i] < p[i+1] < p[i+ 2]  or p[i+2] < p[i+1] < p[i]:
        count +=1
print(count)