n = int(input())
a = list(map(int, input().split()))
cnt = [0]*(n+1)
for i in a:
    cnt[i] += 1
combo1 = [-1]*(n+1)
combo2 = [-1]*(n+1)
total = 0
for i in range(n):
    if combo1[a[i]] == -1:
        c = cnt[a[i]]
        combo1[a[i]] = (c*(c-1)//2)
        combo2[a[i]] = ((c-1)*(c-2)//2)
        total += combo1[a[i]]
'''
print(combo1)
print(combo2)
print(total)
'''
for i in a:
    ans = total - combo1[i] + combo2[i]
    print(ans)