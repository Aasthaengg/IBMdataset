S=input()
T=input()

n=len(S)
count=0
for i in range(n):
    if S[i]!=T[i]:
        count+=1
    else:
        continue
print(count)