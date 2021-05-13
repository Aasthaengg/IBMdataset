abc = sorted(list(map(int, input().split())))

ans = 0
if (abc[1]-abc[0])%2 == 1:
  ans += 1
  abc[1] += 1
  abc[2] += 1

ans += (abc[1]-abc[0])//2
abc[0] += abc[1]-abc[0]
ans += abc[2]-abc[1]
print(ans)