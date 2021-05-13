n,a,b = map(int,input().split())
print((b-a)*(n-2)+1 if (b-a)*(n-2)+1 >= 0 else 0)