n = int(input())
a = list(map(int,input().split()))
b = [0] * n
ans = []
for i in range(n-1, -1, -1):
    if i == n-1:
        b[i] = a[i]
    else:
        sm = sum(b[i::i+1])
        b[i] = abs(a[i] - (sm % 2))
    if b[i] == 1:
        ans.append(i+1)
print(len(ans))
print(' '.join(map(str,ans)))
