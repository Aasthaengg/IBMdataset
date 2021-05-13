def mine(n,m):
    try:
        if n >= 0 and n<=H and m>=0 and m<=W:
            s[n][m] += 1
    except:
        None


H,W = map(int,input().split())
s = [[0 if i == "." else "#" for i in input()]for j in range(H)]
      
for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            mine(i-1,j-1)
            mine(i-1,j)
            mine(i-1,j+1)
            mine(i,j+1)
            mine(i,j-1)
            mine(i+1,j-1)
            mine(i+1,j)
            mine(i+1,j+1)
        else:
            None
      
for k in s:
    a = list(map(str,k))
    print("".join(a))