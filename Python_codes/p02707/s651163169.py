N = int(input())
A = [int(x) for x in input().split()]
A_dict = {}
for a in A:
    if A_dict.get(a):
        A_dict[a] += 1
    else:
        A_dict[a] = 1
B = [0] * N
for i in range(N+1):
    if A_dict.get(i):
        B[i-1] = A_dict[i]
for b in B:
    print(b)
