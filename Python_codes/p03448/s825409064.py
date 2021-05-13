A = int(input())
B = int(input())
C = int(input())
X = int(input())
ans = 0
for i in range(A+1):
    if 500*i > X:
        break
    for j in range(B+1):
        if 500*i + 100*j > X:
            break
        for k in range(C+1):
            if 500*i + 100*j + 50*k > X:
                break
            if 500*i + 100*j + 50*k == X:
                ans += 1

print(ans)