s=input()

l=len(s)

count=0
for i in range(2**(l-1)):
    memory=0
    for j in range(l-1):
        if ((i>>j)&1):
            #print(int(s[memory:j+1]))
            count+=int(s[memory:j+1])
            memory=j+1
    #print(int(s[memory:]))
    count+=int(s[memory:])

print(count)