A, B = map(int, raw_input().split())

if B%A == 0:
    print '{}'.format(A+B)
else: # B%A != 0
    print '{}'.format(B-A)
