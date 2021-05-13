L = [int(num) for num in input().split()]
K = int(input())
L.sort()
L[-1] = L[-1] * (2**K)
print(sum(L))