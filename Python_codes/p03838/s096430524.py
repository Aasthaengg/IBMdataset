A,B=map(int,input().split(' '))
print(min([i if i>0 else 10**10 for i in [B-A,A+B+1,-B+A+2,-B-A+1]]))