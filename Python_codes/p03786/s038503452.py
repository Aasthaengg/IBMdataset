# B - Colorful Creatures
N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
ans = 1
num = sum(A)
for i in range(0,N-1):
    num -= A[i]
    if num*2<A[i]:
        break
    ans += 1
print(ans)