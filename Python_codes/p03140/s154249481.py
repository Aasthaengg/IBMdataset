n = int(input())
A = input()
B = input()
C = input()
cnt = 0
for i in range(n):
    a = A[i]
    b = B[i]
    c = C[i]
    if a == b == c:
        continue
    elif a == b or b == c or c == a:
        cnt += 1
    else:
        cnt += 2
print(cnt)