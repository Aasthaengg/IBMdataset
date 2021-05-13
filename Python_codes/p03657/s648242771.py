a,b = map(int,input().split())
print(["Impossible", "Possible"][a*b*(a+b)%3==0])
