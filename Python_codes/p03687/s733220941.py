import string
def func(a):
    a = a[::-1]
    return a[::-1]
s=input()
s = func(s)
ans=10**9+1
for value in set(s):
    enumerater_value=value+s+value
    var2=0
    var=0
    for i,key in enumerate(enumerater_value):
        if key==value:
            if var2<i-var-1: 
                var2=i-var-1
            var=i
    if ans>var2: 
        ans=var2
print(ans)