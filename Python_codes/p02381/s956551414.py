while 1:
    if input() == '0':
        break
    s = list(map(int, input().split()))
    m = sum(s) / len(s)
    m_2 = sum(i ** 2 for i in s) / len(s)
    print('{0:f}'.format((m_2 - m ** 2) ** 0.5))