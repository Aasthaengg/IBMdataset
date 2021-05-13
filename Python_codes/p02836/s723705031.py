s=input()
if len(s)==1:
    print("0")
    exit()
count=0
for i in range(len(s)//2):
    if not s[i]==s[-1-i]:
        count+=1
print(count)