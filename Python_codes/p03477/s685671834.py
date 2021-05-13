#n = int(input())
#n,k = map(int,input().split())
#x = list(map(int,input().split()))

a,b,c,d =map(int,input().split())

m = a +b -c-d

if m>0:
    print("Left")
elif m ==0:
    print("Balanced")
else:
    print("Right")