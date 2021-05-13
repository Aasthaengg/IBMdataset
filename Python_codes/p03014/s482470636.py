#lamp
import sys
input=sys.stdin.readline
h,w=map(int,input().split())
lists=[]
for i in range(h):
    b=list(input())
    lists.append(b)
    
right=[[0 for i in range(w)] for j in range(h)]
left=[[0 for i in range(w)] for j in range(h)]
up=[[0 for i in range(w)] for j in range(h)]
down=[[0 for i in range(w)] for j in range(h)]

#rightの累積和
for i in range(h):
    for j in range(w-1,-1,-1):
        if j==w-1:
            if lists[i][j]=="#":
                right[i][j]=0
            else:
                right[i][j]=1
        else:
            if lists[i][j+1]=="#":
                if lists[i][j]=="#":
                    right[i][j]=0
                else:
                    right[i][j]=1
            elif lists[i][j+1]==".":
                if lists[i][j]=="#":
                    right[i][j]=0
                else:
                    right[i][j]=right[i][j+1]+1


#leftの累積和
for i in range(h):
    for j in range(w):
        if j==0:
            if lists[i][j]=="#":
                left[i][j]=0
            else:
                left[i][j]=1
        else:
            if lists[i][j]=="#":
                left[i][j]=0
            else:
                left[i][j]=left[i][j-1]+1


#upの累積和
for i in range(w):
    for j in range(h):
        if j==0:
            if lists[j][i]=="#":
                up[j][i]=0
            else:
                up[j][i]=1
        else:
            if lists[j][i]=="#":
                up[j][i]=0
            else:
                up[j][i]=up[j-1][i]+1

                
#downの累積和
for i in range(w):
    for j in range(h-1,-1,-1):
        if j==h-1:
            if lists[j][i]=="#":
                down[j][i]=0
            else:
                down[j][i]=1
        else:
            if lists[j][i]=="#":
                down[j][i]=0
            else:
                down[j][i]=down[j+1][i]+1
                
maxi=0
for i in range(h):
    for j in range(w):
        maxi=max(maxi,right[i][j]+left[i][j]+up[i][j]+down[i][j]-3)
print(maxi)           
