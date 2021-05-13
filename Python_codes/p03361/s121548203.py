h,w = map(int,input().split())
s = [0]*(h+2)
s[0] = ["."]*(w+2)
s[-1] = ["."]*(w+2)
for i in range(1,h+1):
    s[i] = ["."] + list(input()) + ["."]
ans = 1
for i in range(1,h+1):
    for j in range(1,w+1):
        if s[i][j] == "#":
            if s[i-1][j] == "." and s[i+1][j] == "." and s[i][j-1] == "." and s[i][j+1] == ".":
                ans = 0
                break
print(["No","Yes"][ans])