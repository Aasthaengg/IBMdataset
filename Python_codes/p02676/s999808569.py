n=int(input())
s=input()

if len(s) >n :
    print(s[:n]+"...", sep="")
else:
    print(s)
