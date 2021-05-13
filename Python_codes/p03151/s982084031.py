n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
pos = [10**10]+[a[i]-b[i] for i in range(n) if a[i] > b[i]]
neg = [b[i]-a[i] for i in range(n) if a[i] < b[i]]
pos.sort(reverse=True)
pos[0] = 0
for i in range(len(pos)-1): pos[i+1] += pos[i]
need = sum(neg)
ans = len(neg)
for i in range(len(pos)):
    if pos[i] >= need:
        ans += i
        break
else:
    ans = -1
print(ans)