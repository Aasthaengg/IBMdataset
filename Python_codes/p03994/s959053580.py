a=input()
n=len(a)
m=int(input())
ans=""
for i in range(n-1):
  if a[i]=="a":
    ans += "a"
    continue
  x=ord(a[i])-97
  if m>=26-x:
    ans += "a"
    m -= 26-x
  else:
    ans += a[i]
ans += chr((ord(a[n-1])-97+m)%26+97)
print(ans)