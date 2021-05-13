k,a,b=map(int,input().split())
print(max(a+(b-a)*((k-a+1)//2)+(k-a+1)%2,1+k))