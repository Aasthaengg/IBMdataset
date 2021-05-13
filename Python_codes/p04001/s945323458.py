s = input()
n = len(s)
p = []
for i in range(2 ** (n-1)):
    tmp = [' '] * (n-1)
    for j in range(n-1):
        if i >> j & 1:
            tmp[j] = "+"
    p.append(tmp)
ans = []
s = list(s)
s_ = []
for i in range(n):
  if(i == n-1):
    s_.append(s[i])
    break
  s_.append(s[i])
  s_.append(" ")

s__ = []
for i in range(len(p)):
  tmp = s_
  tmp[1::2] = p[i]
  #print(tmp)
  tmp = [a for a in tmp if a != ' ']
  temp = ''.join(tmp)
  #print(temp)
  if("+" in temp):
    ans.append(eval(temp))
  else:
    ans.append(int(temp))
print(sum(ans))
