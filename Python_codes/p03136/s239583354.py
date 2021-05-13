n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
print('Yes' if max(l) < sum(l[1:]) else 'No')