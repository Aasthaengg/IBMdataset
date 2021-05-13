from numpy import*
input();a=array(list(map(int,input().split())))
print(int(min(abs(cumsum(a)-(sum(a)/2)))*2))