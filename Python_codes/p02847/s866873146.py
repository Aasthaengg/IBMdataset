def main():
    DW = 'SUN,MON,TUE,WED,THU,FRI,SAT'
    DW = DW.split(',')

    s = input()
    ind_sun = DW.index('SUN')
    ind_s = DW.index(s)
    diff = ind_sun - ind_s
    print(diff if diff > 0 else diff + 7)


if __name__ == '__main__':
    main()
