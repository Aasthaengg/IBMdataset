while True:
    m, f, r = map(int, input().split())
    sum_score = m + f
    if m != -1 and f != -1:
        if sum_score >= 80:
            print("A")
        elif 65 <= sum_score < 80:
            print("B")
        elif 50 <= sum_score < 65:
            print("C")
        elif 30 <= sum_score < 50:
            if r >= 50:
                print("C")
            else:
                print("D")
        else:
            print("F")
    else:
        if m == -1 and f == -1 and r == -1:
                break
        else:
            print("F")

