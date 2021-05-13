A,B=map(int,input().split())
if (A%3==0)|(B%3==0)|((A+B)%3==0):
    print("Possible")
else:
    print("Impossible")