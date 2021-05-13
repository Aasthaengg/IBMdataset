def LI():
    return list(map(int, input().split()))


N = int(input())
A = LI()
x = []
for i in range(N):
    x.append(A[i]-(i+1))

x.sort()
B = x[N//2]

ans = 0
for i in range(N):
    ans += abs(A[i]-(B+i+1))
print(ans)