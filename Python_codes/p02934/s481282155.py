n = int(input())

lis = map(int,input().split())

total = 0
for i in lis:
    total += 1/i
    
print(1/total)