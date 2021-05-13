s=input()
t=input()

n=len(s)
s_d={}
t_d={}
s_n=[]
t_n=[]
s_cnt=1
t_cnt=1

for s_i, t_i in zip(s,t):

    if s_i in s_d:
        s_n.append(s_d[s_i])
    else:
        s_d[s_i]=s_cnt
        s_cnt+=1
        s_n.append(s_d[s_i])

    if t_i in t_d:
        t_n.append(t_d[t_i])
    else:
        t_d[t_i]=t_cnt
        t_cnt+=1
        t_n.append(t_d[t_i])

print('Yes' if s_n==t_n else 'No')
