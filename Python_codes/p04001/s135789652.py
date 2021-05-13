def separate_and_calc(S,plus_list):
    if plus_list == []:
        return array_to_num(S)
    
    result = 0
    for i in range(len(plus_list)):
        if i == len(plus_list)-1:
            result += array_to_num(S[plus_list[i]:])
        if i == 0:
            result += array_to_num(S[0:plus_list[i]])
            continue
        result += array_to_num(S[plus_list[i-1]:plus_list[i]])

    return result

def array_to_num(S):
    result = 0
    for i in range(len(S)):
        result += int(S[len(S) -1 - i]) * (10**(i))
    return result

S = input()
N = len(S)
result = 0
for bit in range(2**N):
    plus_list = []
    if bit & 1 or bit & (1<<N):
        continue

    for i in range(N):
        if (bit & (1<<i)):
            plus_list.append(i)
    
    result += separate_and_calc(S,plus_list)
    
    # print(" }")
print(result)