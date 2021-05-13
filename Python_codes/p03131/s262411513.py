k,a,b=map(int,input().split())
c=k-a+1
print(max(k+1,a+(c//2)*(b-a)+c%2))