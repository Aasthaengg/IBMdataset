from bisect import bisect_left

n = int(input())
l = sorted(list(map(int, input().split())))

#aを1番短い辺、bを2番めに短い辺とする
cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        c_i = bisect_left(l, l[i] + l[j])
        cnt += c_i - (j+1)

print(cnt)