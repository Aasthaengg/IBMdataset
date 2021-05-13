X=input()
X=X.split()
str=input()
ans=int(X[1])-1
exact=str[ans].lower()
before=str[0:ans]
after=str[ans+1:]
print(before+exact+after)