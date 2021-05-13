n = int(input())
a = list(map(int,input().split()))
MAX = 10**6+1

is_divided = [0]*MAX 
is_appeared = [0]*MAX

for i in range(n):
  if not is_divided[a[i]]:
    if not is_appeared[a[i]]:
      is_appeared[a[i]] = 1
      k = a[i]*2
      while k < MAX:
        is_divided[k] = 1
        k += a[i]
    else:
      is_divided[a[i]] = 1
      
ans = 0      
for i in range(n):
  if not is_divided[a[i]]:
    ans += 1
print(ans)