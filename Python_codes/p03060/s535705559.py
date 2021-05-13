n = int(input())
m = list(map(int, input().split()))
k = list(map(int, input().split()))
    
counter = 0
    
for i in range(n):
    me = m[i] - k[i]
    if me > 0:
        counter += me
    
print(counter)