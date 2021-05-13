n = int(input())
a = list(map(int,input().split()))
ans = []
b = [0] * n

for i in range(1,n+1)[::-1]:
    sum_i = sum(b[(i-1)::i])
    if sum_i%2 != a[i-1]:
        ans.append(i)
        b[i-1] = 1

print(len(ans))
if len(ans) != 0:
    print(*ans)