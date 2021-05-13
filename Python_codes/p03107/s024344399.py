def resolve():
    s = input()
    cnt_zero = s.count('0')
    cnt_one = s.count('1')

    print(min(cnt_one, cnt_zero) * 2)
    
resolve()