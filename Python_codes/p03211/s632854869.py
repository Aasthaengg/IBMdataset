S = input()
m = 0
for i in range(len(S)):
    if i == 0:
        m = abs(int(S[i: i + 3]) - 753)
    elif i == len(S) - 2:
        break
    else:
        m = min(m, abs(int(S[i: i + 3]) - 753))
    # print(m)    



print(m)    
