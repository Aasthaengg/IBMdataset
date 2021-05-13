a = list(map(int,input().split()))
if(a[0]%3==0):
    print("Possible")
elif(a[1]%3==0):
    print("Possible")
elif((a[0]+a[1])%3==0):
    print("Possible")
else:
    print("Impossible")