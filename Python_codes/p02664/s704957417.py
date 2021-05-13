t=input()

def score(t):
  count=0
  for i in range(len(t)-1):
    if t[i]=='D':
      count+=1
    if t[i]=='P'and t[i+1]=='D':
      count+=1
  return count

hold=0

t_tr=t.replace('?','D')
#if hold<=score(t_tr):
#  hold=score(t_tr)
#  t_hold=t_tr

print(t_tr)