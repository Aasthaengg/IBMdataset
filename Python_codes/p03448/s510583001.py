A = int(input().strip())
B = int(input().strip())
C = int(input().strip())
X = int(input().strip())

count = 0

for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            if a*500 + b*100 + c*50 == X:
                count += 1

print(count)