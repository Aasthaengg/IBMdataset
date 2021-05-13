n = int(input())
a = list(map(int,input().split()))
cum_a = [0]
cum_b = [0]
here_a = 0
here_b = 0
for i in range(n):
    cum_a.append(abs(here_a-a[i]) + cum_a[i])
    here_a = a[i]
    cum_b.append(abs(here_b - a[n-1-i]) + cum_b[i])
    here_b = a[n-1-i]
cum_a.append(abs(a[-1])+cum_a[-1])
cum_b.append(abs(a[0]) + cum_b[-1])
here = 0
a.append(0)
for i in range(n):
    l = cum_a[i]
    r = cum_b[n-1-i]
    move = abs(here-a[i+1])
    here = a[i]
    print(l+r+move)
