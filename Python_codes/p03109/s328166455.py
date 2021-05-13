def resolve():
    yyyy, mm, dd = list(map(int, input().split("/")))
    if yyyy < 2019 or (yyyy==2019 and mm < 4) or (yyyy==2019 and mm == 4 and dd <= 30):
        print("Heisei")
    else:
        print("TBD")

if '__main__' == __name__:
    resolve()