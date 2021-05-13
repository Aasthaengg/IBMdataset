a = input()
b = input()

a_len = len(a)
b_len = len(b)

huku = []

for i in range(a_len):
    if a_len != b_len and i==a_len-1:
        huku.append(a[i])
        break
    else:
        huku.append(a[i])
        huku.append(b[i])
for i in range(len(huku)):
    print(huku[i],end="")