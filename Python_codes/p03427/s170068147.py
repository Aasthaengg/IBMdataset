n=input()
l=len(n)-1
if int(n)==(int(n[0])+1)*10**l-1:
    print(int(n[0])+9*l)
else:
    print(int(n[0])+9*l-1)