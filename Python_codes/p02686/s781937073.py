# **************************************************************************** #
#                                                                              #
#                                            __   __ .____  .__  __.  ____     #
#    F-bracketSequencing.py                 |  | |  ||  _ \ |  \/  | /    |    #
#                                           |  | |  || |_| || \  / ||  ,--'    #
#    By: ayahyao <y.anas1997@gmail.com>     |  | |  ||  __/ | |\/| ||  |       #
#                                           |  `-'  || |    | |  | ||  `--.    #
#    Created: 2020/05/10 18:38 by Anas       \_____/ |_|    |_|  |_| \____|    #
#    Updated: 2020/05/10 18:42 by Anas                                         #
#                                                                              #
# **************************************************************************** #

def     process(tab, beginning, end):
    total = beginning
    for i in tab:
        if (i[1] > total or total + i[0] < 0):
            return ("No")
        total += i[0]
    if (total == end):
        return ("Yes")
    return ("No")

def     parsing(N):
    beginning, ending = 0,0
    clean = 0
    total = 0
    tab = []

    for i in range(N):
        s = input()
        before, after = 0, 0
        for j in s:
            if (j == '('):
                after += 1
            elif (j == ')'):
                if (after > 0):
                    after -= 1
                else:
                    before += 1
        if (before == 0 and after > 0):
            beginning += after
        elif (after == 0 and before > 0):
            ending += before
        elif (before > 0 or after > 0):
            tab.append((after - before, before, after))
        else:
            clean += 1
        total += before - after
    tab = sorted(tab)[::-1]
    return tab, total, beginning, ending, clean


N  = int(input())
tab, total, beginning, ending, clean = parsing(N)
if (total == 0 and N == 1):
    res = "Yes"
elif ((total != 0) or ((min(beginning, ending) == 0 and clean == 0) 
                 or (max(beginning, ending) == 0 and clean == 1))):
    res = "No"
else:
    res = process(tab, beginning, ending)
print(res)
