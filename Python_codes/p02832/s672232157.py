N = int(input())
A = [int(x) for x in input().split()]

i = 1
for a in A:
    if a == i:
        i += 1
if i == 1:
    print('-1')
else:
    count = i-1
    print(N-count)
