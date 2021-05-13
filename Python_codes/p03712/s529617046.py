h,w=map(int,input().split())
s,a,x="#"*(w+1),"#","#\n#"
for i in range(h):
	a+=input()+x

print("#"+s,a+s,sep="\n")