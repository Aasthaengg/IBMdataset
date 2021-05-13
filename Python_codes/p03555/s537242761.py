S_list = [input() for i in range(2)]
S = S_list[0]
S_reverse = S[::-1]
if S_reverse == S_list[1] :
    result = "YES"
else:
    result ="NO"
print(result)