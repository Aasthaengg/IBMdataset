
#!/usr/bin/python
# -*- coding: utf-8 -*-

S = input()

ans = 0

a = 0

for i in range(0,len(S)):
    if S[i] == "W":
        ans += i-a
        a += 1
    
print(ans)