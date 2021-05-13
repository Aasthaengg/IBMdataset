N = int(input())
A = input()
B = input()
C = input()
ans = 0
for i in range(N) :
    s = [A[i], B[i], C[i]]
    li = [s.count(s[j]) for j in range(3)]
    ans += 3 - max(li)
print(ans)
