S = input()

abs_list = []

for i in range(len(S)-2):
    num = int(S[i]+S[i+1]+S[i+2])
    abs_i = abs(753-num)
    abs_list.append(abs_i)
    
print(min(abs_list))