import math
n,k=map(int,input().split());input();print([math.ceil((n-k)/(k-1))+1,1][n==k])