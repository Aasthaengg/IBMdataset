k, a, b = map(int, input().split())
q, r = divmod(k-a+1, 2)
print(max(q*(b-a) + r + a, k+1))