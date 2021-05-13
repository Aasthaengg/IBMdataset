from collections import Counter
n = int(input())
a = list(map(int,input().split()))
counter =dict(Counter(a))
c_key =list(counter.keys())
c_value =list(counter.values())
cnt = 0
sl = len(c_value)
for i in range(sl):
  if int(c_key[i]) <  c_value[i]:
      cnt += (c_value[i]- int(c_key[i]))
  elif int(c_key[i]) >  c_value[i]:
 	  cnt += c_value[i] 
print(cnt)