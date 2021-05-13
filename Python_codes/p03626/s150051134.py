n = int(input())
s1 = input()
s2 = input()
ans = 1
ch1 = 1
N = 1000000007
s1+='?'

if s1[0]==s1[1]:
    ch2=2
    ans=6
    s=3
else:
    ch2=1
    ans=3
    s=2

for i in range(s,n+1):
        if s1[i]==s1[i-1]:
            ch1+=1
        else:
            if ch1 ==1:
                if ch2==2:
                    ans*=1
                else:
                    ans=ans*2%N
            else:
                if ch2==2:
                    ans=ans*3%N
                else:
                    ans=ans*2%N
            ch2=ch1
            ch1=1

print(ans)
