s=input()
t=s[::-1]

n=len(s)

num=n//2
count=0

for i in range(num):
    if s[i]!=t[i]:
        count+=1
        
print(count)