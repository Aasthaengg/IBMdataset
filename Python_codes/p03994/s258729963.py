from collections import deque
s=input()
money=int(input())
ans=deque()

d = dict(zip([chr(i) for i in range(97, 97+26)], range(0,26)))
d_r = dict(zip(range(0,26),[chr(i) for i in range(97, 97+26)]))

s_hash = deque([d[i] for i in s])

while len(s_hash)>0:
    #print(money,s_hash,ans)
    n = s_hash.popleft()
    if (money >= 26 - n) & (n != 0):
        ans.append(0)
        money -= 26 - n
    else:
        ans.append(n)
#print(money,s_hash,ans)
money = money % 26
while money>0:
    n = ans.pop()
    ans.append((n+money) % 26)
    money = 0

print("".join([d_r[i] for i in ans]))