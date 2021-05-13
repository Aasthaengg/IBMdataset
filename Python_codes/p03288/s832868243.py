r = int(input())
if 2800 <= r:
    print('AGC')
else:
    print('ABC' if r < 1200 else 'ARC')