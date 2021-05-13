n = int(input())
arr = [int(a) for a in input().split()]
s = sum(arr)
m = s // 2

tmp = 0
for a in arr:
    if tmp + a >= m:
        ans = min(s-tmp*2, (tmp+a)*2-s)
        break
    tmp += a

print(ans)
