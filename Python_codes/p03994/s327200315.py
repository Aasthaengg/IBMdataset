s = list(input())
k = int(input())
t = list(map(lambda x:ord(x)-ord("a"),s)) #a-zを0-25に正規化

for i in range(len(t)):
  diff = 26-t[i] #aになるまでの差
  if diff != 26 and diff <= k: 
    t[i]+=diff
    k-=diff
  else:
    continue

t[-1]+=k #k余りを一番最後に足す

u = "".join(list(map(lambda x:chr((x%26+ord("a"))),t)))
print(u)