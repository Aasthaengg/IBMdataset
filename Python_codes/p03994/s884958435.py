from collections import deque
s = input()
k = int(input())
a = ord("a")
l = deque(list())
l1 = []
for i in range(len(s)):
  s1 = s[i]
  l.append(((a+26)-ord(s1))%26)
#print(l)
while k!=0:
    if len(l)!=0:
        t = l.popleft()
        if k>=t:
            l1.append("a")
            k -= t
        else:
          if t=="a":
            l1.append(t)
          else:
            l1.append(chr((ord('a')-t+26)))
    else:
      k %= 26
      l1[-1] = chr(int(ord(l1[-1])+k))
      k = 0
l2 = []
if len(l)>=1:
  for t in l:
    t %= 26
    if t==0:
      l2.append("a")
    else:
      l2.append(chr((ord('a')-t+26)))
  l1 += l2
print("".join(l1))