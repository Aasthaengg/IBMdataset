K,A,B= map(int,input().split())

ans = 1
if (B-A) <= 2:
  ans += K

else:
  if B - A <=2:
    ans += K
  else:
    ans += A - 1
    if (K-(A-1)) % 2 == 0:
      ans += (((K-(A-1))//2)) * (B - A)
    else:
      ans += (((K-(A-1))//2)) * (B - A) + 1

print(ans)