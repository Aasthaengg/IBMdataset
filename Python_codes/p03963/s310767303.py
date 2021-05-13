from math import pow

n,k=map(int,input().split())
print(int(k*pow(k-1,n-1)))