n=int(raw_input())
i = 1
print "",
while(i<=n):
    x=i
    if x%3 is 0:
        print i,
    elif x%10 is 3:
        print i,
    elif (x/10)%10 is 3:
        print i,
    elif (x/10**2)%10 is 3:
        print i,
    elif (x/10**3)%10 is 3:
        print i,
    elif (x/10**4)%10 is 3:
        print i,
    i = i+1