A,B=map(int,input().split())
c=min(B+A-1,1000000)
d=max(B-A+1,-1000000)
print(" ".join(list(map(str,list(range(d,c+1))))))