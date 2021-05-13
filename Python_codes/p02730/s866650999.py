s=input()
#s="akasaka"

def kaibun(x):
    ans=1
    for i in range(len(x)//2):
        if x[i]!=x[-i-1]:
            ans=0
            break
    return ans
n=len(s)
a1=kaibun(s)
a2=kaibun(s[0:(n-1)//2])
a3=kaibun(s[-1+(n+3)//2:n])

if a1==1 and a2==1 and a3==1:
    print("Yes")
else:
    print("No")
