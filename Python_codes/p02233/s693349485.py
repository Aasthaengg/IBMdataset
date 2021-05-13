n = int(input())

d = {0:1,1:1}
def calc(n):
    if n not in d:
        d[n] = calc(n-2)+calc(n-1)
    return d[n]

for i in range(n):
    calc(i)

print(calc(n))
