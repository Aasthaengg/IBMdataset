(N,),*sp = [s.split() for s in open(0)]

sp = [(s,-int(p),i+1) for i,(s,p) in enumerate(sp)]

for _,_,i in sorted(sp):
    print(i)