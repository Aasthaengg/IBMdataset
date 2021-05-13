N=int(input())
M=10**9+7
batu4=['AGG','AGT','ACG','ATG']
batu3=['AGC','ACG','GAC']
l=['A','G','C','T']
lx=['A','G','T']

def hash_index(s):
  num=0
  length=len(s)
  for i in range(length):
    letter=s[length-1-i]
    if letter=='A': k=0
    elif letter=='G': k=1
    elif letter=='C': k=2
    else: k=3
    num=num+k*4**i
  return num
hash_table=[]
for l1 in l:
  for l2 in l:
    for l3 in l:
      s_a=l1+l2+l3
      if s_a in batu3:
        hash_table.append([set()])
      elif s_a in batu4:
        s=set()
        for l4 in lx:
          s.add(l2+l3+l4)
        hash_table.append(s)
      else:
        s=set()
        for l4 in l:
            s_b=l2+l3+l4
            if not s_b in batu3:
              s.add(s_b)
        hash_table.append(s)
l_p=[1]*64
for l1 in l:
  for l2 in l:
    for l3 in l:
      s=l1+l2+l3
      if s in batu3:
        l_p[hash_index(s)]=0
  
#N>=4
for i in range(N-3):
  l_current=[0]*64
  for j in range(64):
    s_s=hash_table[j]
    for s in s_s:
      if not len(s)==0:
      	l_current[hash_index(s)]=(l_p[j]+l_current[hash_index(s)])%M
  l_p=l_current

num=0
for n in l_p:
  num=(num+n)%M
print(num)