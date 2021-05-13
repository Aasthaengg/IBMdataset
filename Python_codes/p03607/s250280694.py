N = int(input())
a = [input() for _ in range(N)]
a = sorted(a)
#print(a)
c = 0
ans = 0
for i in range(N):
    c += 1
    if i == N-1:
        if c % 2 == 1:
            ans += 1
    elif a[i] != a[i+1]:
        #print(a[i])
        if c % 2 == 1:
            ans += 1
        c = 0

print(ans)
