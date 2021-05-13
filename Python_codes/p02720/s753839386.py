K = int(input())
from collections import deque

X = deque([1,2,3,4,5,6,7,8,9])

for i in range(1,K+1):
    ans = X.popleft()
    if ans%10!=0:
        temp = ans*10 + (ans%10)-1
        X.append(temp)

    temp = ans*10 + (ans%10)
    X.append(temp)
    
    if ans%10!=9:
        temp = ans*10 + (ans%10)+1
        X.append(temp)

print(ans)