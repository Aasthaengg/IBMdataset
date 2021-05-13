import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

num_list = [i+1 for i in range(N)]

a = 1
for i in list(itertools.permutations(num_list)):
    if P==i:
        break
    else:
        a += 1
b = 1
for i in list(itertools.permutations(num_list)):
    if Q==i:
        break
    else:
        b += 1

if a-b>=0:
    print(a-b)
else:
    print(-a+b)