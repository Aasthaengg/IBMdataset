I=input;n=int(I());s='%d\n';i,j=0,n-1;a,b=I(s%i),I(s%j)
while 1:
 k=(j+i+1)//2;c=I(s%k)
 if(k-i)%2==(a==c):j=k
 else:a=c;i=k