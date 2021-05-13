import copy
def main():
    N = int(input())
    A = [int(a) for a in input().split()]

    money = 1000
    stock = 0
    day = 0

    while day < len(A) - 1:
        if A[day + 1] - A[day] > 0:
            cur = copy.deepcopy(day)
            while day < (len(A) - 1):
                if A[day + 1] - A[day] < 0:
                    break
                else:
                    day += 1

            r, m = divmod(money, A[cur])
            stock += r
            money -= r * A[cur]
            money += stock * A[day]
            stock = 0

        elif A[day + 1] - A[day] < 0:
            cur = copy.deepcopy(day)
            while day < (len(A) - 1):
                if A[day + 1] - A[day] > 0:
                    break
                else:
                    day += 1

            if day < len(A) - 1:
                r, m = divmod(money, A[day])
                stock += r
                money -= r * A[day]

        elif A[day + 1] - A[day] == 0:
            day += 1

    print(money)

if __name__ == "__main__":
    main()