def resolve():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    kane=0
    if a>=b:
        kane+=b
    else:
        kane+=a
    if c>=d:
        kane+=d
    else:
        kane+=c
    print(kane)

resolve()