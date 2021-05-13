N,P = list(map(int, input().split()))
a = list(map(int, input().split()))
num_odd = sum([i%2 == 1 for i in a])
num_even = N - num_odd
 
ce = 2 ** num_even
co = 2 ** (num_odd - 1)
if num_odd == 0:
    co = P^1
print(co * ce)