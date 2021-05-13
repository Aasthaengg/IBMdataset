n = int(input())
a = [int(xi) for xi in input().split()]

sum = 0
pm = 0
min = 10**10
for xi in range(n):
    if a[xi]<0: pm+=1
    sum += abs(a[xi])
    if abs(a[xi])<min :min=abs(a[xi])
    # print(a[xi], sum, min)

if pm%2 ==1: sum-=min*2

print(sum)
