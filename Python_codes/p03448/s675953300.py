A = int(input())
B = int(input())
C = int(input())
X = int(input())
an = 0
for i in range(A+1):
    for t in range(B+1):
        for u in range(C+1):
         if 500*i + 100*t + 50*u == X:
             an += 1
print(an)