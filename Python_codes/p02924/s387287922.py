
N = int(input())

calc_N =  N-1

if calc_N % 2 == 1:
    O = calc_N // 2
    output = (1+calc_N) * O + O + 1
else :
    O = calc_N // 2
    output = (1+calc_N) * O
    
print(output)