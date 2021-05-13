while(True):
	H,W=list(map(int,input().split()))
	if H==0 and W==0:
		break
	top=""
	for i in range(W):
		top+="#"
	top+="\n"
	mid="#"
	for i in range(W-2):
		mid+="."
	mid+="#\n"
	s=top
	for i in range(H-2):
		s+=mid
	s+=top
	print(s)