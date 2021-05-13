def a(t,i):
    if i == n-1:
        return sum(map(int,t.split("+")))
    return a(t+s[i+1],i+1)+ a(t+"+"+s[i+1],i+1)

s = input()
n = len(s)
i=0
print(a(s[0],0))
