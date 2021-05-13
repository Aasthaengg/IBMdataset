n = int(input())
ls = [0]*87
for i in range(n+1):
    if i == 0:
        ls[i] = 2
    elif i == 1:
        ls[i] = 1
    else:
        ls[i] = sum(ls[i-2:i])
print(ls[n])