p=[int(input()) for i in range(5)]
q=[10*(0--i//10) for i in p]
res=10**6
for i in range(5):
    res =min(res,sum(q)-q[i]+p[i])
print(res)
