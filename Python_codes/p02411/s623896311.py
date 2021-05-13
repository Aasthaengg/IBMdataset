while True:

    m, f, r = map(int, input().split())
    if m==f==r== -1:
        break
    result = ""
    sum = m + f
    
    if (m==-1)or(f==-1):
        result = "F"
    elif sum >= 80:
        result = 'A'
    elif sum>= 65:
        result = "B"
    elif sum>=50:
        result = "C"
    elif sum>= 30:
        result="D"
        if r>=50:
            result = 'C'
    else:
        result = 'F'

    print("{}".format(result))