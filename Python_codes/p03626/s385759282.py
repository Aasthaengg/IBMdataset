from collections import defaultdict,deque
import math
def main():
    n = int(input())
    s1 = input()
    s2 = input()
    s = ""
    i=0
    while(i<n):
        if(s1[i]==s2[i]):
            s+="|"
            i+=1
        else:
            s+="="
            i+=2
        if(i>=n):
            break
    res = 0
    if(s[0]=="|"):
        res = 3
    else:
        res = 6
    MOD = 10**9 + 7
    for i in range(1,len(s)):
        if(s[i-1]=="|" and s[i]=="|"):
            res *= 2
        elif(s[i-1]=="|" and s[i]=="="):
            res *= 2
        elif(s[i-1]=="=" and s[i]=="|"):
            res *= 1
        else:
            res *= 3

        res%=MOD
    print(res)

if __name__ == '__main__':
    main()
