from collections import Counter
h,w,n = map(int,input().split())
need = []
append = need.append
for i in range(n):
    a,b = map(int,input().split())
    for x in range(-2,1):
        for y in range(-2,1):
            s = a + x
            t = b + y
            if 1 <= s <= h-2 and 1 <= t <= w-2:
                append(s*10**9 + t)

data = Counter(need).most_common()
ans = [0 for i in range(10)]
for x,y in data:
    ans[y] += 1

print((h-2)*(w-2)-sum(ans))
for i in ans[1:]:
    print(i)