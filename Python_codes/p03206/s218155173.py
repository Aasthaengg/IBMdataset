d=int(input())
result='Christmas'
n=25
while n>=22:
    if n>d:
        result+=' Eve'
    n-=1
print(result)