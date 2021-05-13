a,b,c,d=map(int, input().split()) 
if d**2 >=(c-a)**2:
    print("Yes")
elif (d**2>=(c-b)**2 and d**2>=(b-a)**2):
    print("Yes")
else:
    print("No")