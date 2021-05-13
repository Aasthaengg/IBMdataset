D = {"A":"T","T":"A","C":"G","G":"C"}
b = input().strip()
x = ""
for i in range(len(b)):
    x += D[b[i]]
print(x)