k, x = map(int, input().split())

l = [x - i for i in range(1, k)] + [x + i for i in range(k)]
l.sort()
ans = ''
for n in l:
  ans += str(n) + ' '

print(ans)