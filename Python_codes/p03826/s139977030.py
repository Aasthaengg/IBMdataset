arr_int = [int(s) for s in input().split(" ")]

if(( arr_int[0]* arr_int[1]) > (arr_int[2]* arr_int[3])):
	print(arr_int[0]* arr_int[1] )
else:
	print(arr_int[2]* arr_int[3])