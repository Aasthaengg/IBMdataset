import copy
n = int(input())
a = list(map(int,input().split()))
b = copy.copy(a)
ans_a = 0
ans_b = 0
sum_a = 0
sum_b = 0
for i in range(n):
    if i%2==0:
        if sum_a+a[i]>0:
            tmp = 0
        else:
            tmp = abs(sum_a+a[i])+1
            a[i] += tmp
            ans_a += tmp
    else:
        if sum_a+a[i]<0:
            tmp = 0
        else:
            tmp = abs(sum_a+a[i])+1
            a[i] -= tmp
            ans_a += tmp
    sum_a+=a[i]
    if i%2==1:
        if sum_b+b[i]>0:
            tmp = 0
        else:
            tmp = abs(sum_b+b[i])+1
            b[i] += tmp
            ans_b += tmp
    else:
        if sum_b+b[i]<0:
            tmp = 0
        else:
            tmp = abs(sum_b+b[i])+1
            b[i] -= tmp
            ans_b += tmp
    sum_b+=b[i]
#print(a)
#print(sum_a)
print(min(ans_a,ans_b))