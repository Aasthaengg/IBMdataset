N,A,B = map(int,input().split())
count = 0
for i in range(1,N+1):
    add = sum(list(map(int, str(i))))
    if A <= add and add <= B:
        count += i
        
print(count)
