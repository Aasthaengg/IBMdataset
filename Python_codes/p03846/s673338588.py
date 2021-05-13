i=input
n=int(i())
print([0,pow(2,n//2,10**9+7)][sorted(map(int,i().split()))==[(j+n%2)//2*2+1-n%2for j in range(n)]])