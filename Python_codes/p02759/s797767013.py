N = int(input())

q, mod = divmod(N, 2)
if mod == 0:
    print(q)
else:
    print(q+1)