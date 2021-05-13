n,d=map(int,input().split())
kansi=0
if n%(2*d+1)==0:
    kansi=n/(2*d+1)
else:
    kansi=n//(2*d+1)+1
print(int(kansi))