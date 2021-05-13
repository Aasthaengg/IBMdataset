val=0
while 1:
    try:
        a,op,b = input().split()
        a=int(a)
        b=int(b)
        if op=='?': 
            break
        elif op=='+':
            val=a+b
        elif op=='-':
            val=a-b
        elif op=='*':
            val=a*b
        elif op=='/':
            val=a//b
        print(val)
    except EOFError:
        #print("EOFError")
        break