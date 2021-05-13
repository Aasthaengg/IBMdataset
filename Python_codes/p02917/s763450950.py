N = int(input())
a = [1e10]*N
b = list(map(int,input().split()))

for i,num in enumerate(b):
    if a[i] > num:
        a[i] = num
    a[i+1] = num
print(sum(a))