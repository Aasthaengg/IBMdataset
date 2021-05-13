from math import ceil
n,k=map(int,input().split());
print("YNEOS"[ceil(len([i for i in range(1,n+1)])/2)<k::2])