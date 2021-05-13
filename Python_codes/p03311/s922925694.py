N = int(input())
A = list(map(int,input().split()))
B = [a-i for i,a in enumerate(A)]
B.sort()
m = B[N//2]
ans = 0
for b in B:
    ans += abs(m-b)
print(ans)