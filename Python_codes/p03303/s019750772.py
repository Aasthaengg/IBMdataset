s = input()
w = int(input())
ans = []
if len(s)%w == 0:
  for i in range(len(s)//w):
    ans.append(s[w*i])
else:
  for i in range(len(s)//w+1):
    ans.append(s[w*i])
print("".join(ans))