N = int(input())
a = [int(_) for _ in input().split()]

d = {}

for i in range(N):
    if a[i] not in d:
        d[a[i]]=1
    else:
        d[a[i]]+=1
num_odd = 0
num_even= 0

for m in d:
    if d[m] % 2 == 0:num_even+=1
    else:num_odd+=1
print((num_odd+num_even if num_even%2==0 else num_odd +num_even-1))