a,b,c,d,e,f=map(int,input().split())
i=0
answ=0
anss=0
cnt=0
while 100*a*i<=f:
  j=0
  while 100*a*i+100*b*j<=f:
    k=0
    while c*k<=(a*i+b*j)*e:
      l=0
      if (a*i+b*j+c*k+d*l)!=0:
        if cnt<100*(c*k+d*l)/(a*i+b*j+c*k+d*l):
          if (a*i+b*j)*100+c*k+d*l<=f:
            cnt=100*(c*k+d*l)/(a*i+b*j+c*k+d*l)
            answ=(a*i+b*j)*100
            anss=c*k+d*l
      l=((a*i+b*j)*e-c*k)//d
      if l>0:
        if (a*i+b*j+c*k+d*l)!=0:
          if cnt<100*(c*k+d*l)/(a*i+b*j+c*k+d*l):
            if (a*i+b*j)*100+c*k+d*l<=f:
              cnt=100*(c*k+d*l)/(a*i+b*j+c*k+d*l)
              answ=(a*i+b*j)*100
              anss=c*k+d*l
      l=(f-(a*i+b*j)*100-c*k)//d
      if l>0:
        if (a*i+b*j+c*k+d*l)!=0:
          if cnt<100*(c*k+d*l)/(a*i+b*j+c*k+d*l):
            if c*k+d*l<=(a*i+b*j)*e:
              cnt=100*(c*k+d*l)/(a*i+b*j+c*k+d*l)
              answ=(a*i+b*j)*100
              anss=c*k+d*l
      k=k+1
    j=j+1
  i=i+1
temp=0
i=0
while 100*a*i<=f:
  j=0
  while 100*a*i+100*b*j<=f:
    temp=max(temp,100*a*i+100*b*j)
    j=j+1
  i=i+1
if 100*a+c>f:
  print(100*a,0)
elif temp//100*e<c:
  print(temp,0)
else:
  print(answ+anss,anss)