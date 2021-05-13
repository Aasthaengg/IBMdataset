S = input()
K = int(input())

tmp = []

s_len = len(S)
for i in range(s_len):
    for j in range(i,i+min(K,s_len-i)):
        #print(i, j)
        #print(S[i:j+1])
        tmp.append(S[i:j+1])

str_set = set(tmp)

for i,s in enumerate(sorted(str_set)):
    if i == K-1:
        print(s)
        break