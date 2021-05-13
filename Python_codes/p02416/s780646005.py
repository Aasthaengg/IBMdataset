while True:
    n = raw_input()
    if n == '0':
        break
    num = map(int,list(n))
    j= 0
    for i in num:
	j += i
    print j