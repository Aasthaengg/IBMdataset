import collections
n = int(input())
v = [int(x) for x in input().split()]
v_odd, v_evn = [], []
for i in range(n):
  if i%2==0:
    v_odd.append(v[i])
  else:
    v_evn.append(v[i])
v_odd_cnt = collections.Counter(v_odd)
v_evn_cnt = collections.Counter(v_evn)
if len(v_odd_cnt) == len(v_evn_cnt) == 1:
  if v[0] == v[1]:
    print(n//2)
    exit()
  else:
    print(0)
    exit()
max_kv_odd = max(v_odd_cnt.items(), key=lambda x: x[1])
max_kv_evn = max(v_evn_cnt.items(), key=lambda x: x[1])
if max_kv_odd[0] == max_kv_evn[0]:
  if len(v_odd_cnt) == 1:
    v_evn_cnt.pop(max_kv_evn[0])
    max_kv_evn_tmp = max(v_evn_cnt.items(), key=lambda x: x[1])
    print(n-max_kv_odd[1]-max_kv_evn_tmp[1])
    exit()
  if len(v_evn_cnt) == 1:
    v_odd_cnt.pop(max_kv_odd[0])
    max_kv_odd_tmp = max(v_odd_cnt.items(), key=lambda x: x[1])
    print(n-max_kv_odd_tmp[1]-max_kv_evn[1])
    exit()
  v_odd_cnt_tmp = v_odd_cnt
  v_evn_cnt_tmp = v_evn_cnt
  v_odd_cnt_tmp.pop(max_kv_odd[0])
  v_evn_cnt_tmp.pop(max_kv_evn[0])
  max_kv_odd_tmp = max(v_odd_cnt_tmp.items(), key=lambda x: x[1])
  max_kv_evn_tmp = max(v_evn_cnt_tmp.items(), key=lambda x: x[1])
  a = max_kv_odd[1] + max_kv_evn_tmp[1]
  b = max_kv_evn[1] + max_kv_odd_tmp[1]
  print(n-max(a, b))
  exit()
print(n-max_kv_odd[1]-max_kv_evn[1])
