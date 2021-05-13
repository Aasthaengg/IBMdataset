first_high, first_width,second_high, second_width = map(int,input().split())

first_place = first_high * first_width
second_place = second_high * second_width

if first_place >= second_place:
	print(first_place)
else:
	print(second_place)