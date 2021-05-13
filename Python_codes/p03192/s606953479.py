count=0
n=int(input())

for i in range(4):
    if n%10 == 2:
        count = count+1
    n = int(n/10)
        
print(count)
