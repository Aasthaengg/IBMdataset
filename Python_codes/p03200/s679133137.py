#!/usr/bin/env python3

S = input()

ans = 0;
for i, s in enumerate(S):
    if s == "B":
        ans += len(S) - i
        
for i in range(1,S.count("B")+1):
    ans -= i
print(ans)
               
    
