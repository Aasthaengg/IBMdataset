# CODE FESTIVAL 2016 予選 C: B – K個のケーキ / K Cakes
K, T = [int(s) for s in input().split()]
a = [int(s) for s in input().split()]

max_index = a.index(max(a))

print(max(a[max_index] - 1 - (K - a[max_index]), 0))