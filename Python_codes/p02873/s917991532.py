s=input()

result=[0]*(len(s)+1)


for index,ss in enumerate(s):
    if ss=="<":
        result[index+1]=result[index]+1
#print(result)
for i in range(len(s)):
    index=len(s)-i-1
    if s[index]==">":
        result[index]=max(result[index],result[index+1]+1)
print(sum(result))




#1 0 -1
#2 1 0
    


