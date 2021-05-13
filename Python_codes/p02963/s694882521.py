s = int(input())
if round(s**0.5)**2==s:
    tmp = round(s**0.5)
    print(0, 0, tmp, 0, 0, tmp)
    exit()
i = int(s**0.5)+1
for j in range(i, 0, -1):
    if i*j<s:
        print(0, 0, i, 1, i*(j+1)-s, j+1)
        break