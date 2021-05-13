S=input()
right=[0]*(len(S)+1)
for i in range(len(S)):
    if S[i]=="<":
        right[i+1]=right[i]+1
left=[0]*(len(S)+1)

for j in range(len(S)-1,-1,-1):
    if S[j]==">":
        left[j]=left[j+1]+1
        
total=0
for k in range(len(S)+1):
    total+=max(right[k],left[k])
print(total)