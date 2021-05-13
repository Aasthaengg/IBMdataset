N = int(input())
ans = []

num = N-1
while(True):
  if num >= 26:
    ans.append(num%26)
    num = num//26-1
  else:
    ans.append(num)
    break
answer = ""
for n in ans[::-1]:
  answer += chr(97+n)
print(answer)