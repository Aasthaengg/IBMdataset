def resolve():
    S = input()
    week = [ "SUN","MON","TUE","WED","THU","FRI","SAT" ]
    print(7-week.index(S))

if '__main__' == __name__:
    resolve()