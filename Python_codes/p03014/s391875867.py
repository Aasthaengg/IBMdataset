h,w = map(int,input().split())
s =["#"*(w+2)] + ["#"+input()+"#" for i in range(h)] + ["#"*(w+2)]
# print(s)
ans = 1
opt = [(0,1),(0,-1),(1,0),(-1,0)]
s2 = [[0]*(w+2) for i in range(h+2)]
s3 = [[0]*(w+2) for i in range(h+2)]
for i in range(1,h+1):
    for j in range(1,w+1):
        if s[i][j] == "." and s2[i][j] == 0:
            cnt = 0
            for k in opt[0:2]:
                tempy = i
                tempx = j
                while s[tempy+k[0]][tempx+k[1]] == ".":
                    cnt += 1
                    tempy += k[0]
                    tempx += k[1]
            for k in opt[0:2]:
                tempy = i
                tempx = j
                while s[tempy+k[0]][tempx+k[1]] == ".":
                    s2[tempy+k[0]][tempx+k[1]] += cnt
                    tempy += k[0]
                    tempx += k[1]
            s2[i][j] += cnt
        if s[i][j] == "." and s3[i][j] == 0:
            cnt = 0
            for k in opt[2:4]:
                tempy = i
                tempx = j
                while s[tempy+k[0]][tempx+k[1]] == ".":
                    cnt += 1
                    tempy += k[0]
                    tempx += k[1]
            for k in opt[2:4]:
                tempy = i
                tempx = j
                while s[tempy+k[0]][tempx+k[1]] == ".":
                    s3[tempy+k[0]][tempx+k[1]] += cnt
                    tempy += k[0]
                    tempx += k[1]
            s3[i][j] += cnt
        ans = max(ans,1+s2[i][j]+s3[i][j])
# print(s2)
print(ans)