k,a,b=map(int,input().split())
print(k+1 if a+1>=b or k<a else 1+(k-a+1)//2*(b-a)+(k-a+1)%2+a-1)