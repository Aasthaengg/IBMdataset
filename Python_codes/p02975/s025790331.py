N = int(input())
a = list(map(int,input().split()))
a.sort()
x = [10**9+1,0]
y = [10**9+1,0]
z = [10**9+1,0]
for i in range(N):
    if x[0] == a[i]:
        x[1] += 1
    else:
        if x[1] == 0:
            x[0] = a[i]
            x[1] += 1
        elif y[0] == a[i]:
            y[1] += 1
        else:
            if y[1] == 0:
                y[0] = a[i]
                y[1] += 1
            elif z[0] == a[i]:
                z[1] += 1
            else:
                if z[1] == 0:
                    z[0] = a[i]
                    z[1] += 1

ans = 'No'
if x[0] == 0:
    if x[1] == N:
        ans = 'Yes'
    elif x[1]*2 == y[1] and x[1] + y[1] == N:
        ans = 'Yes'
if x[1] == y[1] == z[1] and x[1] + y[1] + z[1] == N and x[0]^y[0]^z[0] == 0:
    ans = 'Yes'

print(ans)