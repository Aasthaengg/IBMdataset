#B問題
O = input()
E = input()
result = [""] * (len(O) + len(E))
for i in range(len(O)):
    result[2 * i] = O[i]
for i in range(len(E)):
    result[2 * i + 1] = E[i]
print("".join(result))