n = int(input())
v_list = list(map(int,input().split()))
v_list_odd = v_list[::2]
v_list_ev = v_list[1::2]
import collections
c_odd = collections.Counter(v_list_odd)
c_even = collections.Counter(v_list_ev)

c_odd = sorted(c_odd.items(),key=lambda x:x[1],reverse = True)
c_even = sorted(c_even.items(),key=lambda x:x[1],reverse = True)
if c_odd[0][0] != c_even[0][0]:
  print(n - c_odd[0][1] - c_even[0][1])
else:
  if len(c_odd) == 1 and len(c_even) == 1:
    print(n - c_odd[0][1])
  elif len(c_odd) == 1:
    print(n - c_odd[0][1] - c_even[1][1])
  elif len(c_even) == 1:
    print(n - c_odd[1][1] - c_even[0][1])
  else:
    print(n - max(c_odd[1][1] + c_even[0][1],c_odd[0][1] + c_even[1][1]))