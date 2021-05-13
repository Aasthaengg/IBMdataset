def resolve():
    inp = input()
    li = list(map(lambda x: int(x), inp.split(" ")))
    num = li[1]//li[0]
    print(min(num, li[2]))
    
resolve()