import sys
n,m = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
if n>=m:
    print(0)
    sys.exit()
dis = [x[i+1]-x[i] for i in range(m-1)]
dis.sort()
print(sum(dis[:m-n]))