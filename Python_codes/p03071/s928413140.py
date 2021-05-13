n=list(map(int,input().split()))
if n[0]==n[1]:
    print(n[0]*2)
else:
    print(max(n)*2-1)