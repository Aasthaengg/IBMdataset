n = int(input())
A = list(map(int, input().split()))
cnt = 0
for a in A:
  if a%2 != 0: cnt += 1
print("YES" if cnt%2==0 else "NO")