tn=list(map(int,list(input())))
for i in range(0,16,2):
  if sum(x*[1,-1][i>>k&1] for k,x in enumerate(tn))==7:
    s=''.join(list(['+','-'][i>>k&1]+str(tn[k]) for k in range(1,4)))
    print(str(tn[0])+s+'=7')
    break
