try:
    a,p=map(int, input().split())
    assert 0<=a,p<=100
    print(((a*3)+p)//2)
except AssertionError:
    print('')
