s=input()
res=[]
for i in range(len(s)-2):
    res += [abs(int(s[i:i+3])-753)]
print(min(res))