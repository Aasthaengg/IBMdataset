n = int(input())

count = 0
for i in range(1,n//2+1):
    if not n - i == i:
        count +=1
        
print(count)