s=input()
for i in range(2,len(s),2):
    x=s[:-i]
    leng=len(x)
    if x[:leng//2] == x[leng//2:]:
        print(leng)
        break