MOD = 10 ** 9 + 7

n = int(input())
s1 = input()
s2 = input()

ans = 1
index =0
if s1[0] == s2[0]:
  ans *= 3
  index = 1
else:
  ans *= 3 * 2
  index = 2
  
while index < n:
  if s1[index-1] == s2[index-1]:
    ans *= 2
    if s1[index] == s2[index]:
      index += 1
    else:
      index += 2
      
  else:
    if s1[index] == s2[index]:
      index += 1
    else:
      ans *= 3
      index += 2
  
  ans %= MOD
      
print(ans)