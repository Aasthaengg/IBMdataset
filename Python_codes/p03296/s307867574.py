
N = int(input())

s = 1

a = list(map(int,input().split()))
a.append(None)

ans = 0

for i in range(N):

    i += 1
    if a[i-1] == a[i]:
        s += 1

    else:
        ans += s//2
        s = 1

print (ans)
