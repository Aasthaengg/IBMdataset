N = int(input())
K = str(N)
L = len(K)
K.split(',', L)
num_list = list(map(int, K))
A = 0

for i in range(L):
    A += num_list[i]

if A % 9 == 0:
    print("Yes")
else:
    print("No")
