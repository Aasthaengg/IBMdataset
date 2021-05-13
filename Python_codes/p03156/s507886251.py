_,a,b,*p=map(int,open(0).read().split())
print(min(eval("sum(%s for j in p)"%["j<=a","a<j<=b","b<j"][i]) for i in range(3)))