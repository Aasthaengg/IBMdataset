C = [""]*3
res = ""
for i in range(3):
    C[i] = str(input())
    res = res + C[i][i]
print(res)
