n, m, x = [int(w) for w in input().split()]
a_li = [int(w) for w in input().split()]

print(min(len([w for w in a_li if 0 <= w <= x]),
          len([w for w in a_li if min(x, n) <= w <= max(x, n)])))
