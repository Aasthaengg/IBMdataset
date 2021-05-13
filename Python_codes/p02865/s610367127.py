n = int(input())
count = 0
max_n = int(n/2) if n%2 ==0 else int((n+1)/2)
for i in range(1, max_n):
    count+=1
print(count)