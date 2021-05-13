n = int(input())

d = [int(input()) for i in range(n)]

d.sort()
count=1
if n>1:
    for i in range(n-1):
        if d[i] < d[i+1]:
            count+=1
    
print(count)
