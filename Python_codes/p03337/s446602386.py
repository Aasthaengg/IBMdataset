X = input()
X = list(map(int, X.split()))
A = X[0]
B = X[1]
so = A+B
su = A-B
m = A*B
maior = so
if (su > maior):
    maior = su
if (m > maior):
    maior = m
print(maior)