h,w=map(int,input().split())
a=[input() for i in range(h)]
ans="Yes"
for i in range(h):
    for j in range(w):
        if i==0:
            if j==0:
                if a[i][j]=="#":
                    if h>=2:
                        if not a[i+1][j]=="#":
                            if w>=2:
                                if not a[i][j+1]=="#":
                                    ans="No"
                    elif w>=2:
                        if not a[i][j+1]=="#":
                            ans="No"
                    else:
                        ans="No"
                                    
            elif j==(w-1):
                if a[i][j]=="#":
                    if a[i][j-1]!="#":
                        if h==1:
                            ans="No"
                        else:
                            if a[i+1][j]!="#":
                                ans="No"
            else:
                if a[i][j]=="#":
                    if a[i][j-1]!="#" and a[i][j+1]!="#":
                        if h==1:
                            ans="No"
                        else:
                            if a[i+1][j]!="#":
                                ans="No"
            
        elif i==(h-1):
            if j==0:
                if a[i][j]=="#":
                    if a[i-1][j]!="#":
                        if w==1:
                            ans="No"
                        else:
                            if a[i][j+1]!="#":
                                ans="No"
                
            elif j==(w-1):
                if a[i][j]=="#":
                    if a[i][j-1]!="#" and a[i-1][j]!="#":
                        ans="No"
                
            else:
                if a[i][j]=="#":
                    if a[i][j-1]!="#" and a[i-1][j]!="#" and a[i][j+1]!="#":
                        ans="No"
                
        else:
            if j==0:
                if a[i][j]=="#":
                    if a[i-1][j]!="#" and a[i+1][j]!="#":
                        if w==1:
                            ans="No"
                        else:
                            if a[i][j+1]!="#":
                                ans="No"
            elif j==(w-1):
                if a[i][j]=="#":
                    if a[i][j-1]!="#" and a[i-1][j]!="#" and a[i+1][j]!="#":
                        ans="No"
            else:
                if a[i][j]=="#":
                    if a[i][j-1]!="#" and a[i][j+1]!="#" and a[i-1][j]!="#" and a[i+1][j]!="#":
                        ans="No"

print(ans)