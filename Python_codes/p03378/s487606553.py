n,m,x = map(int, input().split())

p = map(int, input().split())

count1 = count2 = 0

for i in p:
    if 0 < i <= x:
        count1 += 1
    elif x <= i <= n:
        count2 += 1
    
print(min(count1,count2))