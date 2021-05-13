a,b = map(int,input().split())
print(["Impossible", "Possible"][a*b%3==0 or (a+b)%3==0])