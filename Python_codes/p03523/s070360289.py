s=input()
ans=set()
def two(k):
	 qq="0"*(9-len(bin(k)[2:]))+bin(k)[2:]
	 return qq

for i in range(1,2**9):
	p=""
	for j in range(9):
		if two(i)[j]=="1":
			p+="AKIHABARA"[j]
		if "KI" in p and "H" in p and "B" in p and "R" in p:
			ans.add(p)
if s in ans:
	print("YES")
else:
	print("NO")