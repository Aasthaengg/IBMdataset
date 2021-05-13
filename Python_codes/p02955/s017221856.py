n, k = map(int,input().split())
a = list(map(int,input().split()))


def d(x):
    l = []
    for i in range(1, int(x**0.5)+1):
        if x%i==0:
            l.append(i)
            if i != x//i:
                l.append(x//i)
    l.sort(reverse=True)
    return l

s = d(sum(a))
for i in s:
    x = [0 for k in range(n)]
    for j in range(len(a)):
        x[j] = a[j] % i
    x.sort()
    l = [0 for k in range(n+1)]
    r = [0 for k in range(n+1)]
    for j in range(n+1):
        if j == 0:
            l[0] = 0
            r[n-0] = 0
        else:
            l[j] = l[j-1] + x[j-1]
            r[n-j] = r[n-j+1] + (i-x[n-j])
    ans = 1
    for j in range(n+1):
        if l[j] == r[j] and l[j] <= k:
            ans = i
            print(ans)
            exit()
