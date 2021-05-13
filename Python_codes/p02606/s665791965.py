L, R, d = list(map(int, input().split()))
diff = R - L + 1
ans = 0
l = [None for _ in range(diff)]
for i in range(diff):
   l[i] = L + i
   if l[i] % d == 0:
      ans += 1
print(ans)