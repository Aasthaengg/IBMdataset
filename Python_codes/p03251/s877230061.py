a,b,c,d=map(int,input().split())
e=list(map(int,input().split()))
f=list(map(int,input().split()))
for i in range(c+1,d+1):
    if max(e)<i and min(f)>=i:
        print('No War')
        exit()
print('War')