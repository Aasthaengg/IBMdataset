def get_contest(r):
    if r < 1200:
        print('ABC')
    elif r<2800:
        print('ARC')
    else:
        print('AGC')
        
R=int(input())

get_contest(R)