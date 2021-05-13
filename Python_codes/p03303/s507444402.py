# coding: utf-8
#N, m, d = map(int,input().split())
#N = int(input())
s = input()
#s = list(map(str,input().split()))
#a, b = map(int,input().split())
#P = list(map(int,input().split()))
w = int(input())
ans = ""
if w==1:
    ans = s
else:
    for i in range(len(s)):
        if (i+1)%w==1:
            ans += s[i]
    
print(ans)