def print2(A,S): #print2(int or str a[:][:], str)
    for i in range(len(A)):
        b = [str(n) for n in A[i][:]]
        print(S.join(b))

h,w = map(int,input().split())
s = [0]*(h+2)
s[0] = ["."]*(w+2)
s[-1] = ["."]*(w+2)
for i in range(h):
    s[i+1] = ["."] + list(input()) + ["."]
ans = [[0 for j in range(w)] for i in range(h)]
for i in range(1,h+1):
    for j in range(1,w+1):
        if s[i][j] == "#":
            ans[i-1][j-1] = "#"
        else:
            for y in range(-1,2):
                for x in range(-1,2):
                    if s[i+y][j+x] == "#":
                        ans[i-1][j-1] += 1
print2(ans,"")