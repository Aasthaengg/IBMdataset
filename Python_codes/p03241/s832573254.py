def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

n,m = map(int,input().split())

if m%n==0:
    print(m//n)
else:
    arr = sorted(divisor(m))
    # print(arr)
    for i in arr:
        if i >= n:           
            print(m//i)
            exit()