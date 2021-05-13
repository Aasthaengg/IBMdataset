n=int(input())
a=list(map(int,input().split()))
ans=0
count_plus=0
sum_plus=0
for i in range(n):
    if i%2 == 0:
        if a[i]+sum_plus > 0:
            sum_plus += a[i]
        else:
            count_plus += 1-a[i]-sum_plus
            sum_plus = 1
    else:
        if a[i]+sum_plus < 0:
            sum_plus += a[i]
        else:
            count_plus += 1+a[i]+sum_plus
            sum_plus=-1

count_minus=0
sum_minus=0
for i in range(n):
    if i%2 != 0:
        if a[i]+sum_minus > 0:
            sum_minus += a[i]
        else:
            count_minus += 1-a[i]-sum_minus
            sum_minus = 1
    else:
        if a[i]+sum_minus < 0:
            sum_minus += a[i]
        else:
            count_minus += 1+a[i]+sum_minus
            sum_minus=-1
            
print(min(count_plus,count_minus))