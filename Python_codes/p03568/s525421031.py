N = int(input())
A = [int(i) for i in input().split()]
dim = 1

for val in A:
    if(val%2 == 0):
        dim *= 2
    else:
        dim *= 1
print(3**N-dim)