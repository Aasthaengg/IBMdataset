n,c,k=map(int,input().split())
t = [int(input()) for _ in range(n)]
a = [0]*(n+1)
i = 0
j = 0
t = sorted(t)
while i < n:
    now = t[i]
    a[j] += 1
    i += 1
    while a[j] <c and i<n:
        if now<=t[i]<=now+k:
            a[j] += 1
        else:
            break
        i += 1
    j += 1
print(len([x for x in a if x != 0]))