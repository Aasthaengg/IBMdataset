s=input()
n=len(s)
def f(s):
    m=len(s)
    for i in range(-(-m//2)):
        if s[i]!=s[-1-i]:
            return False
    return True

if f(s) and f(s[:(n-1)//2]) and f(s[((n+3)//2)-1:]):
    print("Yes")
else:
    print("No")