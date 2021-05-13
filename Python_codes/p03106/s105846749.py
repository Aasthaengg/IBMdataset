A, B, K = input().split()
A = int(A)
B = int(B)
K = int(K)

min = A if A <= B else B

list = []
for i in range(1, min+1):
    if A % i == 0 and B % i == 0:
        list.append(i)

print(list[len(list)-K])