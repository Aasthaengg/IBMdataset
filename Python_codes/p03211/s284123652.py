a = input()

la = len(a)

res = 753

for i in range(la-2):
    temp = a[i:i+3]
    tempp = abs(int(temp)-753)
    res = min(res,tempp)

print(res)