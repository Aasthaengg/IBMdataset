from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
###############################################################################\
s=input()
bool=True
for i in range(len(s)):
    if i%2==0:
        if s[i]=="R" or s[i]=="U" or s[i]=="D":
            continue
        else:
            bool=False
            break
    else:
        if s[i]=="L" or s[i]=="U" or s[i]=="D":
            continue
        else:
            bool=False
            break

if bool is True:
    print("Yes")
else:
    print("No")
