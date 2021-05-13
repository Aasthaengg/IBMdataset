S = input()
n = len(S)
rcount = 0
result = [0] * len(S)
for i in range(n-1):
    if S[i] == 'R' and S[i+1] == 'L':
        if rcount % 2 == 1:
            result[i+1] += rcount // 2 + 1 + 1
        else:
            result[i+1] += rcount // 2 + 1
        result[i] = rcount // 2 + 1 
        rcount = 0
    elif S[i] == 'R' and S[i+1] == 'R':
        rcount += 1
lcount = 0
#print (result)
for i in range(n-1, 0, -1):
    #print (S[i-1], S[i], lcount)
    if S[i] == 'L' and S[i-1] == 'R' and lcount > 0:
        if lcount % 2 == 1:
            result[i-1] += lcount // 2 + 1 
        else:
            result[i-1] += lcount // 2 
        result[i] += lcount // 2 
        lcount = 0
    elif S[i] == 'L' and S[i-1] == 'L':
        lcount += 1
print (" ".join(list(map(str, result))))