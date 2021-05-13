s='CODEFESTIVAL2016'
cnt=0
ss=input()
for i in range(16):
	cnt+=(s[i]!=ss[i])
print(cnt)