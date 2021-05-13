try:
    age,money=map(int, input().split())
    assert 0<=age<=100 and 2<=money<=1000 and money%2==0
    if age<=5:
        print('0')
    elif 6<=age<=12:
        print(money//2)
    else:
        print(money)
except AssertionError:
    print('')

