import sys;print"\n".join("%d %d"%(lambda x:(x[2],x[0]/x[2]*x[1]))((lambda f,x:(x[0],x[1],f(f,x[0],x[1])))(lambda f,a,b:a%b==0 and b or f(f,b,a%b),map(int,s.split(' '))))for s in sys.stdin)