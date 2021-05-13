N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
before = 10**3
ans = 0
for i in A:
    if i - before == 1:
        ans += C[before-1]
    before = i
ans += sum(B)
print(ans)