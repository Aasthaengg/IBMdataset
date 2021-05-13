H,W = map(int,input().split())
A = [input().split() for i in range(H)]


X = "#"*(W+2)

#print(H,W,A)


for i in range(H):
	A[i][0] = "#" + A[i][0] +"#"

print(X)
for i in range(H):
	print(A[i][0])
print(X)
