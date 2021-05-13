S = list(input())
runlength = []
temp = S[0]
if len(set(S)) == 1:
    print(0)
    exit() 
for i in range(1,len(S)):
    if temp != S[i]:
        runlength.append(temp)
        temp = S[i]
runlength.append(temp)
print(len(runlength)-1)