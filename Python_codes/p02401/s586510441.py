import sys

for i in sys.stdin:
    a,op,b = i.replace('/','//').split()
    if op == "?":
        break
    else:
        print(eval(a+op+b))