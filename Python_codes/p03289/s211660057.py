import sys, math, itertools, collections, bisect 
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

s = input()
chk_C = False
if s[0] != "A":
    print("WA")
    exit()
else:
    for i in range(len(s)):
        if i == 0:
            pass
        else:
            if s[i] == "C" and chk_C == False and i >= 2 and i <= len(s)-2:
                chk_C = True
                pass
            elif s[i] == s[i].lower():
                pass
            else:
                print("WA")
                exit()
    if chk_C == True:
        print("AC")
    else:
        print("WA")