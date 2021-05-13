N = int(input())



print(0)
S_0 = input() #椅子0の性別を確認

start = -1
goal= N
m = (start+ goal) //2



while True:
    print(m)
    q = (input())
    if q == "Vacant":
        exit(0)

    if m %2 == 0: #偶数番目の椅子だったら→S_0と一致
        if q == S_0:
            start = m
        else:
            goal = m
    else:
        if q == S_0:
            goal = m
        else:
            start = m
    m = (start+ goal) //2
