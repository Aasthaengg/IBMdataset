import math
s=input()
w=int(input())
ans=""
for i in range(math.ceil(len(s)/w)):
    ans+=s[i*w]
print(ans)