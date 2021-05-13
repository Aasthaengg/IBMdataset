h,  w =  map(int, input().split())
a = []
a.append("."*(w+2))
for _ in  range(h):
    a.append("."+input()+".")
a.append("."*(w+2))

ans  = "Yes"
for i in range(h+2):
    for j in  range(w+2):
        if a[i][j] == "#":
            if not(a[i-1][j] == "#" or a[i+1][j] == "#" or a[i][j-1] == "#" or a[i][j+1] == "#"):
                ans = "No"
                break
print(ans)