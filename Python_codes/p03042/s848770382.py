def main():
    S = str(input())
    front = int(S[0:2])
    latter = int(S[2:4])
    if front < 13 and latter < 13 and (front > 0 and latter > 0):
        print('AMBIGUOUS')
    elif front < 13 and latter < 100 and front > 0:
        print('MMYY')
    elif front < 100 and latter < 13 and latter > 0:
        print('YYMM')
    else:
        print('NA')
main()