H,W=map(int, input().split())
S=[list(input()) for _ in range(H)]
l=[]
flag=0

for h in range(H):
	for w in range(W):
		if S[h][w]=="#":
			if h>0:
				l.append(S[h-1][w])
			if h<H-1:
				l.append(S[h+1][w])
			if w>0:
				l.append(S[h][w-1])
			if w<W-1:
				l.append(S[h][w+1])
			if "#" not in l:
				flag=1
				break
			l=[]

print("Yes" if flag==0 else "No")