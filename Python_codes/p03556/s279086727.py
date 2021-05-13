n = int(input())
a = 0
for i in range(n+1):
    if i*i <= n:
        a = i*i
    else:
        break
print(a)
