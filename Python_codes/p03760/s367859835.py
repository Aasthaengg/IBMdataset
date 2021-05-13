o = str(input())
e = str(input())
w = ""
for i in range(len(e)):
    w += (o[i]+e[i])
if len(o)-len(e) == 1:
    w += o[len(o)-1]
print(w)