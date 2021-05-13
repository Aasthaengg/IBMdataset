n = int(input())
a = list(map(int, input().split()))
ans = [0]*n
count = 0
for i in range(n-1, -1, -1):
    c = sum([ans[j] for j in range(i, n, i+1)])%2
    if c != a[i]:
        count+=1
        ans[i] = 1
print(count)
ans = [i+1 for i in range(n) if ans[i]==1]
if count > 0:
    print(' '.join(map(str, ans)))