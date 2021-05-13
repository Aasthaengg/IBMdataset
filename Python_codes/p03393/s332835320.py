from string import*;from itertools import*;b=ascii_lowercase;s=r=input();t=s[::-1];d=0
if len(s)>25:d=-[p*len(list(k))for p,k in groupby(i<j for i,j in zip(t,t[1:]))][0]-2;s,b,r=s[:d],s[d+1:],b[:ord((s*2)[d])-97]
print(-(d<-26)or s+sorted(set(b)-set(r))[0])