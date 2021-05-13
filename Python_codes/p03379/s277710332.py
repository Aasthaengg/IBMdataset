n = int(input())
li = list(map(int,input().split()))
lia = sorted(li)
med1,med2 = lia[n//2-1],lia[n//2]
for i in range(n):
    if li[i] <= med1:
        print(med2)
    else:
        print(med1)