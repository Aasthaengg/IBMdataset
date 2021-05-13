N, L = map(int, input().split())
l = [x+L-1 for x in range(1, N+1)]
l_2 = list(map(abs, l))
min_index = l_2.index(min(l_2))

l[min_index] = 0
print(sum(l))