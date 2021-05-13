st = str(input())
dum = st.split()
d = int(dum[0])
t = int(dum[1])
s = int(dum[2])

tv = float(d / t)
if tv <= s:
    print('Yes')
else:
    print('No')