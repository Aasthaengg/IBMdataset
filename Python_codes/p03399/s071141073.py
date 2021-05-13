A = int(input())
B = int(input())
C = int(input())
D = int(input())
minvalue1 = 10000
minvalue2 = 10000
m = [A, B]
n = [C, D]
for i in range(len(m)):
    if m[i] < minvalue1:
        minvalue1 = m[i]
for z in range(len(n)):
    if n[z] < minvalue2:
        minvalue2 = n[z]
print(minvalue1+minvalue2)