import itertools
n = int(input())
l = list(map(int, input().split()))
num = 0
for i,h,j in itertools.combinations(l,3):
    if i+h>j and h+j>i and j+i>h and j!=i and i!=h and h!=j:
        num += 1
print(num)