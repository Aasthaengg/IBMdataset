N = int(input())
l = list(map(int, input().split()))

l.sort()
mid_id = int((N / 2) - 1)
ans = l[mid_id+1] - l[mid_id]

print(ans)
