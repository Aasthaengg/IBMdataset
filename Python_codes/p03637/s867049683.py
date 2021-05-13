n  = int(input())
lst = list(map(int, input().split()))

count4 = 0
count2 = 0

for i in lst:
    if i%4==0:
        count4+=1
    elif i%2==0:
        count2+=1
count1 = n-count4-count2

if count2==0 and count4>=count1-1:
    print("Yes")
elif count2!=0 and count4>=count1:
    print("Yes")
else:
    print("No")
