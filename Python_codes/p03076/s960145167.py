l=[int(input()) for i in range(5)]
s=[]
for i in range(5):
    s.append((((l[i]//10)+1)*10-l[i])%10)
print(sum(l)+sum(s)-max(s))