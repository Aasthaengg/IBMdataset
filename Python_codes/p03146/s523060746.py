s=int(input())
def f(x):
    if x%2==0:
        return x//2
    else:
        return 3*x+1
a=s
ans=[s]
for i in range(10**6+5):
    a=f(a)
    if a in ans:
        print(i+2)
        exit()
    ans.append(a)
    
    
