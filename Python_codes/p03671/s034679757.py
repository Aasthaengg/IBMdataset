a, b, c = list(map(int, input().split()))
m = [a, b, c]
maxvalue = 0
for i in range(len(m)):
    if m[i] > maxvalue:
        maxvalue = m[i]
print(a+b+c-maxvalue)