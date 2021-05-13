def input_multiple_number():
    return map(int, input().split())

def input_multiple_number_as_list():
    return list(map(int, input().split()))

N,A,B = input_multiple_number()
list_X = input_multiple_number_as_list()

ans = 0 
for i in range(1,len(list_X)):
	ans += min((list_X[i]-list_X[i-1])*A,B)

print(ans)