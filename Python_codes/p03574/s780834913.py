#6re
h,w = map(int,input().split())
s = []
s.append(list("." for i in range(w+2)))
for i in range(h):
    s.append(list("."+input()+"."))
s.append(list("." for i in range(w+2)))
ans = [[0 for j in range(w) ] for i in range(h) ]
    
for i in range(1,h+1):
    for j in range(1,w+1):
        if s[i][j] != "#":
            for m in range(i-1,i+2):
                for n in range(j-1,j+2):
                    if s[m][n] == "#":
                        ans[i-1][j-1] += 1
        else:
            ans[i-1][j-1] = "#"
                
for i in range(h):
    for j in range(w):
        ans[i][j] = str(ans[i][j])
        
for i in range(h):
    print("".join(ans[i]))