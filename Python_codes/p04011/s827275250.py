n,k,x,y=[int(input())for _ in [0]*4]
print(n*x) if n<k else print(y*(n-k)+x*k)
