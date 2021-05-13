n, m = map(int, input().split())

submit = 1<<m
time = (1900*m)+100*(n-m)
print(time*submit)
