#n = int(input())
#n,k = map(int,input().split())
#x = list(map(int,input().split()))

x,a,b = map(int,input().split())

t = abs(x-a)-abs(x-b)

if t>0:
    print("B")
else:
    print("A")