s=input()
from collections import Counter
c=Counter(s)
a_cnt=c["a"]
b_cnt=c["b"]
c_cnt=c["c"]
if abs(a_cnt-b_cnt)<=1 and abs(b_cnt-c_cnt)<=1 and abs(c_cnt-a_cnt)<=1:
  print("YES")
else:
  print("NO")