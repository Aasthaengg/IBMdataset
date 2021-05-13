n = int(input())
a = list(map(int,input().split()))

s = 0
count1 = 0
for i in range(n):
    s+=a[i]
    if i%2==1:
        if s<=0:
            count1 += -s + 1
            s = 1
    else:
        if s>=0:
            count1 += s + 1
            s = -1

s = 0
count2 = 0
for i in range(n):
    s+=a[i]
    if i%2==0:
        if s<=0:
            count2 += -s + 1
            s = 1
    else:
        if s>=0:
            count2 += s + 1
            s = -1

print(min(count1,count2))