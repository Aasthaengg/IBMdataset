import math

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


s = input()
#a = list(map(int, input().split()))

mode=0
ans=0
anum=0
banum=0
for i in range(len(s)):
    if(mode==0 and s[i]=='A'):
        anum+=1
    elif(mode==1 and s[i]=='A'):
        anum=1
        mode=0
    elif(mode==0 and s[i]=='B'):
        mode=1
    elif(mode==1 and s[i]=='B'):
        mode=0
        anum=0
    elif(mode==0 and s[i]=='C'):
        mode=0
        anum=0
    elif(mode==1 and s[i]=='C'):
        mode=0
        ans += anum
    #print(ans)

print(ans)
