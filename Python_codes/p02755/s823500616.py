A, B = map(int, input().split())
ans = 0
for k in range(1001):
  if int(ans*0.08) == A and int(ans*0.1) ==B:
    print(ans)
    exit()
  else:
    ans += 1
print(-1)