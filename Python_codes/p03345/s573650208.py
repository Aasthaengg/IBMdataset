a,b,c,k=map(int,input().split())
res=0
if k%2==1:res=b-a
else:res=a-b
if(res<10**18):
        print(res)
        exit()
else:
        print("unfair")
        exit()

