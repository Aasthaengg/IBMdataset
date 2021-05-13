s=input()
count=0
for i in range(len(s)//2):
    if s[i]==s[len(s)-1-i]:
        count+=1
print(len(s)//2-count)