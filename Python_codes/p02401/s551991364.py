import sys

for i in sys.stdin:
    if "?" in i:
        break
    else:
        print(eval(i.replace("/","//")))