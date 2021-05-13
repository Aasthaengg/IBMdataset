def main():

    score_list = []
    while True:
        m, f, r = map(int, input().split())
        if [m, f, r] == [-1, -1, -1]: break
        score_list.append([m, f, r])
    
    for item in score_list:
        [m, f, r] = item
        total = m + f
        if [m, f, r] == [-1, -1, -1]: break
        elif m == -1 or f == -1:
            result = 'F'
        elif total < 30:
            result = 'F'
        elif total < 50:
            if r >= 50:
                result = 'C'
            else:
                result = 'D'
        elif total < 65:
            result = 'C'
        elif total < 80:
            result = 'B'
        else:
            result = 'A'
        print(result)

main()