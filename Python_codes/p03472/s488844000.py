N, H = map(int, input().split())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i], B[i] = map(int, input().split())
a = max(A)
B.sort()
ans = 0
while len(B) > 0 and B[-1] >= a and H > 0:
    H -= B.pop()
    ans += 1
    if H <= 0:
        print(ans)
        exit()
print(ans+(-(-H//a)))