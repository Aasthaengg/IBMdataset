S=input()

def f(s):
    sum=0
    if len(s)==1:
        return int(s)
    for i in range(1,len(s)):
        sum+=(2**(len(s)-i-1))*int(s[:i])+f(s[i:])
    return sum+int(s)

print(f(S))