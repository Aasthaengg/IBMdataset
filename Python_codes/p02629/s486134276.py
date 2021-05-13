from collections import deque

n = int(input())
tmp = 2 
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans = deque()
len1 = 0
for i in range(1,100):
    if (n <= 26 ** i):
        len1 = i
        break
    else:
        n = n - 26**i

n = n -1
for i in range(len1):
    tmp = n % 26
    ans.appendleft(alpha[tmp])
    n = int(n / 26)


for i in range(len(ans)):
    print(ans.popleft(),end ="")
