def resolve():


    a,b,c=map(int,input().split())
    print(max(0,c-max(0,a-b)))
resolve()