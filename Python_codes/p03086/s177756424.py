s = str(input())
w = ""
l = []
for i in s:
    if i=='A' or i=='C' or i=='G' or i=='T':
        w += i
    else:
        l.append(len(w))
        w = ""
l.append(len(w))
print(max(l))