N = int(input())
N_2 = N//2

v = list(map(int, input().split()))
v_odd = [v[2*i+1] for i in range(N_2)]
v_evn = [v[2*i] for i in range(N_2)]

lst_odd = [0] * 100001
lst_evn = [0] * 100001

for vi in v_odd:
  lst_odd[vi] += 1
  
for vi in v_evn:
  lst_evn[vi] += 1
  
tpl_odd = [(lst_odd[i+1], i+1) for i in range(100000)]
tpl_evn = [(lst_evn[i+1], i+1) for i in range(100000)]

tpl_odd.sort(reverse=True)
tpl_evn.sort(reverse=True)
if tpl_odd[0][1] != tpl_evn[0][1]:
  print(N - tpl_odd[0][0] - tpl_evn[0][0])
else:
  print(N - max(tpl_odd[1][0]+tpl_evn[0][0], tpl_odd[0][0]+tpl_evn[1][0]))
  

