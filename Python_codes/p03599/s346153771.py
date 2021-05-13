def resolve():
    A, B, C, D, E, F = list(map(int, input().split()))
    target = 100*E/(100+E)
    result_con = -float("inf")
    result_all = 0
    result_suger = 0
    for i in range(31):
        for j in range(31):
            for k in range(101):
                for l in range(101):
                    total = 100*A*i + 100*B*j + C*k + D*l
                    suger = C*k + D*l
                    if total == 0:
                        continue
                    if total - suger == 0:
                        break
                    if total > F:
                        break
                    con = 100*suger/total
                    if con > target:
                        break
                    if result_con < con:
                        result_con = con
                        result_all = total
                        result_suger = suger
    print("{} {}".format(result_all, result_suger))


if '__main__' == __name__:
    resolve()