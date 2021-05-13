W = input().lower()
#print(W)
t=0

while(1):
	char_list = list(x for x in input().split())
	#print(char_list)
	if char_list[0] == 'END_OF_TEXT':
		break
	
	for i in range(len(char_list)):
		if W == char_list[i].lower():
			t += 1

print(t)