s=input()
t=input()
ds=dict()
dt=dict()
ss=''
st=''
for i in s:
    if i not in ds:
        ds[i]=str(len(ds))+' '
    ss+=ds[i]
for i in t:
    if i not in dt:
        dt[i]=str(len(dt))+' '
    st+=dt[i]
#print(ss,st)
print('Yes' if ss==st else 'No')
#print(ds,dt)