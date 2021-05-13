n, k = map(int,input().split())
s = input()
s += '#'
lis = []
cnt = 0
for i in range(n):
    cnt += 1
    if s[i] != s[i+1]:
        lis.append(cnt)
        cnt = 0
#print(lis)
val = 0
ans = 0
for i in range(len(lis)):
    if i < 2*k+1:
        val += lis[i]
    else:
        ans += lis[i] - 1
ans += val - 1
print(ans)
