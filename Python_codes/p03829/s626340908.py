N, A, B = map(int, input().split())
# N <= 10**5
# A, B <= 10**9
X = [int(x) for x in input().split()]
# X{i] <= 10**9
#
cost = 0
for i in range(N-1):
    d = X[i+1] - X[i]
    if d*A < B:
        #print(i, ":", d, "A")
        cost += d* A
    else:
        #print(i,":", d, "B")
        cost += B
print(cost)



