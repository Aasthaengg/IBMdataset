n,p = map(int,input().split())
s = input()

ans = 0

ruisekiwa = [0]*(n+1)
ten = 1

if 10 % p == 0:
  for i in range(n):
    if int(s[i]) % p == 0:
      ans += i+1
else:
  for i in range(0,n)[::-1]:#iは(n-1)から0まで降順にループ
    a = int(s[i]) * ten % p
    ruisekiwa[i] = (ruisekiwa[i+1] + a) % p
    ten *= 10
    ten %= p
    
  cnt = [0]*p
  for i in range(0,n+1)[::-1]:
    ans += cnt[ruisekiwa[i]]
    cnt[ruisekiwa[i]] += 1
print(ans)