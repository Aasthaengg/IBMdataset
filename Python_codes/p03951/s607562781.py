n=int(input())
s=str(input())
t=str(input())
 
if s==t:
    print(n)
else:
    for i in range(1,n+1):
        x = s + t[-i:]
        if x[-n:] == t:
            break
    print(len(x))