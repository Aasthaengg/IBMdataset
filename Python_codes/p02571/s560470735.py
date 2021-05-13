s=list(input())
t=list(input())
result=0
#count=0
for i in range(len(s)-len(t)+1) :
    count=0
    for n in range(len(t)):
        if s[i+n]==t[n]:
            count += 1
        #s[i:i+len(t)] == t
    
    if count>result:
        result=count


print(len(t)-result)