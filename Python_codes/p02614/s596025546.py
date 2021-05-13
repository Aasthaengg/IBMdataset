H, W, K = map(lambda x: int(x), input().split())
 
matrix = []
for i in range(H):
	row = input()
	dots = []
	for j in range(W):
		dots.append(row[j])
	matrix.append(dots)


ans = 0
for a in range(1<<H):
    for b in range(1<<W):
        cnt=0 
        for c in range(H):
            if a&(1<<c): 
                for d in range(W):
                 if b&(1<<d): 
                    cnt+=matrix[c][d]=='#'
        ans+=cnt==K
 
print(ans)