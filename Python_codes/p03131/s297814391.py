k,a,b=map(int,input().split())

if k<=a: print(1+k)
else:
    print(max(1+k, b+(k-a-1)//2*(b-a) + (k-a-1)%2))
