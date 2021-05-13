N = int(input())
H = list(map(int,input().split()))

hardle = 0
ans = "Yes"
for i in H:
  if hardle>i:
    ans = "No"
    break
  else:
    if i>hardle:
      hardle=i-1
print(ans)