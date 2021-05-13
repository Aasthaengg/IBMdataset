s = int(input())
a = []
a.append(s)
def f(n):
    if n%2 ==0:
        return int(n/2)
    else:
        return 3*n+1
i = 1        
while f(a[-1]) not in a:
    a.append(f(a[-1]))
    i+=1
#print(i,a)
print(i+1)