T = [int(input()) for _ in range(5)]

L = [-i%10 for i in T]

print(sum(T) + sum(L) - max(L))