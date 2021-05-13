import itertools
A = int(input())
B = int(input())
C = int(input())
X = int(input())

a = list(range(0,A+1))
b = list(range(0,B+1))
c = list(range(0,C+1))

fifty = X/50
ans = 0

for i in itertools.product(a, b, c):
    if 10*i[0]+2*i[1]+i[2] == fifty:
        ans += 1

print(ans)