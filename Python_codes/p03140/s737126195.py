# coding: utf-8
# Your code here!


n = int(input())

al = list(input())
bl = list(input())
cl = list(input())

ans = 0
for i,j,k in zip(al,bl,cl):
    a = [i,j,k]
    if max(a.count(i), a.count(j), a.count(k)) == 1:
        ans += 2
    elif max(a.count(i), a.count(j), a.count(k)) == 2:
        ans += 1
    else:
        pass
    
print(ans)