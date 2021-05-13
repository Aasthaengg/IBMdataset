import collections
n = int(input())
v = list(map(int,input().split()))
v_odd = []
v_even = []
for i,v in enumerate(v):
    if i % 2:
        v_even.append(v)
    else:
        v_odd.append(v)
odd_n = len(v_odd)
even_n = len(v_even)
v_odd = collections.Counter(v_odd)
v_odd = sorted(v_odd.items(), key=lambda x:x[1],reverse=True)
v_even = collections.Counter(v_even)
v_even = sorted(v_even.items(), key=lambda x:x[1],reverse=True)

if v_odd[0] == v_even[0] and 2 <= len(v_odd) and 2 <= len(v_even):
    if v_odd[1][1] < v_even[1][1]:
        v_even.pop(0)
    elif v_odd[1][1] > v_even[1][1]:
        v_odd.pop(0)

num = v_odd[0][0]

ans = odd_n-v_odd[0][1]
st = 0
for i,v in v_even:
    if num == i:
        continue
    else:
        st = v
        break
print(ans+(even_n-st))