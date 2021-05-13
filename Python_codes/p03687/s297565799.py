#!/usr/bin/env python3
# sys.stdin.readline()
import numpy as np
import math
s = input()
def chang(st,string):
    cnt = 0    
    while True:
        if len(set(list(string))) == 1:
            
            return cnt
            break
        
        else:
            stn = ""
            for i in range(len(string)-1):
                if string[i]==st or string[i+1] ==st:
                    stn+=st
                else:
                    stn+=string[i]
            else:
                cnt+=1
                string = stn
                
d = set(list(s))
ans = 100
for i in d:
    ans = min(ans , chang(i,s))
print(ans)


