
S = str(input())
l = len(S)
st = 0
en = 0
for i in range(l):
    if S[i] == 'A':
        st = i
        break
for j in range(l-1,-1,-1):
    #print(j)
    if S[j] == 'Z':
        en = j
        break
#print(st,en)
print(en-st+1)