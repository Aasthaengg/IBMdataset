# input
C = [list(input()) for n in range(3)]

# check
res = "".join([C[n][n] for n in range(3)])
print(res)
