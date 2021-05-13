A = list('CODEFESTIVAL2016')
B = list(input())


t = 0
for i, j in zip(A, B):
    if i != j:
        t += 1
print(t)