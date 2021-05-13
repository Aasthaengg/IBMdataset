s = int(input())
if s == 10**18:
    print(0, 0, 10**9, 0, 1, 10**9)
    exit()
q, r = divmod(s, 10**9)
print(0, 0, 10**9, 10**9-r, 1, q+1)
