n = input()
table =	set()

for i in range(n):
    com	= raw_input().split()
    if(com[0][0] == "i"):
	table.add(com[1])
    else:
	if com[1] in table:
            print("yes")
	else:
            print("no")