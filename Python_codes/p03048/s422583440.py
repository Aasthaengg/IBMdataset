# coding: utf-8
# Your code here!
r , g , b , n = map(int,input().split())
ans = 0
R = -(-n//r)
G = -(-n//g)
for i in range(R+1):
    for j in range(G+1):
        su = n-r*i-g*j
        if n-r*i-g*j < 0:
            break
        else:
            if (su/b).is_integer():
                ans += 1
print(ans)