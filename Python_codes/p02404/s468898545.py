while True:
	H,W=[int(i) for i in input().split(" ")]
	if H==W==0:
		break
	print("#"*(W))
	for h in range(H-2):
		print(("."*(W-2)).join(("#","#")))
	print("#"*(W))
	print()