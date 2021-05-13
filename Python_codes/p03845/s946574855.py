n = int(input())
lt = [int(w) for w in input().split()]
m = int(input())

sum_lt = sum(lt)
for i in range(m):
    p, x = [int(w) for w in input().split()]
    print(sum_lt + x - lt[p - 1])
