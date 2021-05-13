def main():
    n = int(input())
    sp_lst = [0] * n
    for i in range(n):
        sp_lst[i] = list(map(str, input().split()))

    turn_lst = []
    city_lst = []
    for i in range(n):
        city_lst.append(sp_lst[i][0])
    city_lst = list(set(city_lst))
    city_lst.sort()

    number_of_cities = len(city_lst)
    for i in range(number_of_cities):
        city = city_lst[i]
        score_lst = []
        for j in range(n):
            if city == sp_lst[j][0]:
                score_lst.append(int(sp_lst[j][1]))

        score_lst = sorted(score_lst)
        score_lst.reverse()
        number_of_score = len(score_lst)
        for k in range(number_of_score):
            score = str(score_lst[k])
            turn_lst.append(sp_lst.index([city, score]) + 1)

    for i in range(n):
        print(turn_lst[i])

if __name__ == "__main__":
    main()