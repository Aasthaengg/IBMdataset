A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

r = []

if A%10 != 0:
    r.append(10 - A%10)
    A += 10 - A%10
if B%10 != 0:
    r.append(10 - B%10)
    B += 10 - B%10
if C%10 != 0:
    r.append(10 - C%10)
    C += 10 - C%10
if D%10 != 0:
    r.append(10 - D%10)
    D += 10 - D%10
if E%10 != 0:
    r.append(10 - E%10)
    E += 10 - E % 10

if r:
    print(A+B+C+D+E-max(r))
else:
    print(A+B+C+D+E)
