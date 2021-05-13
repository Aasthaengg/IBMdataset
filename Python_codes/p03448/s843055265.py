ct = 0
A = int(input()) ##500円
B = int(input()) ##100円
C = int(input()) ##50円
X = int(input())
for i in range(A,-1,-1):
    for j in range(B,-1,-1):
        for k in range(C,-1,-1):
            if (500*i) + (100*j) + (50*k) == X:
                ct += 1

print(ct)
