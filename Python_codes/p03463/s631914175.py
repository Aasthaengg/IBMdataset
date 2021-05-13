N,A,B=map(int,input().split())
print(("Borys","Alice")[(abs(A-B)-1)%2==1])