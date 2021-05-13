a, b=map(int, input().split())
c=a+b
if c == 24:
    print("0")
elif c >24:
    print(c-24)
else:
    print(c)
