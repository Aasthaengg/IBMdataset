s = list(input())
k = int(input())
t = list(map(lambda x:ord(x)-ord("a"),s))
 
for i in range(len(t)):
  diff = 26-t[i]
  if diff != 26 and diff <= k: 
    t[i]+=diff
    k-=diff
t[-1]+=k
 
u = "".join(list(map(lambda x:chr((x%26+ord("a"))),t)))
print(u)