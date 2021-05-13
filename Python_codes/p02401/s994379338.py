while True:
    s=input().split()
    op=s[1]
    if not (op=="+" or op=="-" or op=="*" or op=="/"):
        break
    a=int(s[0])
    b=int(s[2])
    if op=="+":
        print(a + b)
    elif op=="-":
        print(a - b)
    elif op=="*":
        print(a * b)
    elif op=="/":
        print(int(a / b))
