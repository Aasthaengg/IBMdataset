c=[0]*6**8
for a in[*open(0)][1].split():c[int(a)]+=1
m=max(sum(c[i::i])for i in range(2,6**8))
print(m<sum(c)and'psaeitr'[m>1::2]+'wise'or'not','coprime')