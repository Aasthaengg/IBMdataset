s = input()
l = len(s)
n = int(input())
ans = ["A"]*l
for i in range(l-1):
  if s[i]=="a":
    ans[i]="a"
    continue
  temp = ord("z")-ord(s[i])+1
  if temp <= n:
    n-=temp
    ans[i]="a"
  else:
    ans[i]=s[i]

last = ord(s[l-1])+n
#print(last)
while last>ord("z"):
  last-=26
ans[l-1]=chr(last)
print("".join(ans))