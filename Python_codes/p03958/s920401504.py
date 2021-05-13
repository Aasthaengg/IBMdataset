k,t = map(int, input().split())
a = list(map(int, input().split()))
a = list(reversed(sorted(a)))

for i in range(t-1):
    for j in range(i+1,t):
        if a[i] == 0:
            break
        x = min(a[i], a[j])
        a[i] -= x
        a[j] -= x
print(max(sum(a)-1, 0))