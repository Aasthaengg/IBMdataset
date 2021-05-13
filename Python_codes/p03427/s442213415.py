lst_N = [int(c) for c in input()]
set_N = set(lst_N)
first = lst_N[0]
left = lst_N[1:]
if len(lst_N) == 1: #1桁
    print(lst_N[0])
elif len(set_N) == 1 and lst_N[0] == 9: #all 9
    print(sum(lst_N))
elif first != 9 and len(set(left)) == 1 and left[0] == 9: #9以外＋残り全部９
    all_nine = "9" * (len(left))
    lst_all_nine = [int(c) for c in all_nine]
    print(first + sum(lst_all_nine))
else:
    all_nine = "9" * (len(lst_N) - 1)
    lst_all_nine = [int(c) for c in all_nine]
    print((first-1) + sum(lst_all_nine))