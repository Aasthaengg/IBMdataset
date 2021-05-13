s=list(input())
t=list(input())

for i in range(len(s)):
    p=s.pop(0)
    s.append(p)
    if s==t:
        print("Yes")
        exit()
        
print("No")