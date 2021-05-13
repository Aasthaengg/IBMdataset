N = int(input())
p = [int(input()) for _ in range(N)]

sorted_p = sorted(p)
half_price = int(sorted_p[-1] / 2 )
total_price = 0

for i in range(N-1):
    total_price += sorted_p[i]
total_price += half_price

print(total_price)
