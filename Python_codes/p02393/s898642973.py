S =raw_input()
L = S.split()

a = L[0]
b = L[1]
c = L[2]

a = int(a)
b = int(b)
c = int(c)
l = [a,b,c]
    
min_1 = min(a,b,c)
# print l.remove(min_1)
l.remove(min_1)

min_2 = min(l)

l.remove(min_2)

min_3 = l[0]

min_1 = str(min_1)
min_2 = str(min_2)
min_3 = str(min_3)

print min_1+' '+min_2+' '+min_3