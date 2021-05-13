n=int(input())
jp,bi=0,0
for i in range(n):
    x,u=map(str,input().split())
    if u=='JPY':
        jp+=int(x)
    else:
        bi+=float(x)
print(jp+380000*bi)