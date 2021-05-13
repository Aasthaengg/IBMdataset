n=int(input())
ab=[[0]*2 for ii in range(n)]
for ii in range(n):
	ab[ii][1],ab[ii][0]=map(int,input().split())

#ab = sorted(ab, reverse=True, key=lambda x: x[1])  #[1]に注目してソート
ab.sort(reverse=True)
#print(ab)
r=ab[0][0]
for ii in range(n):
  r=min(ab[ii][0],r)-ab[ii][1]
  if r<0:
    print("No")
    exit()

print("Yes")
