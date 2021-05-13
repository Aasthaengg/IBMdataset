Str = list(input())
q = int(input())

for i1 in range(q):
    Input = input().split()
    Order = Input[0]
    
    if Order == "print":
        a = int(Input[1])
        b = int(Input[2])
        for i2 in range(a, b + 1):
            print(Str[i2], end = '')
        print()
        continue
    
    if Order == "reverse":
        a = int(Input[1])
        b = int(Input[2])
        work = Str[a: b + 1]
        work.reverse()
        Str[a: b + 1] = work
        continue

    if Order == "replace":
        a = int(Input[1])
        b = int(Input[2])
        p = Input[3]
        Str[a: b + 1] = p
        continue