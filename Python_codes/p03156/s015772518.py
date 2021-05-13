n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))
count1 = 0
count2 = 0
count3 = 0

for i in range(n):
    if p[i] <= a:
        count1 +=1
    elif a+1 <= p[i] <= b:
        count2 +=1
    elif b+1 <= p[i]:
        count3 +=1
print(min(count1,count2,count3))