#coding: UTF-8

while True:
    N = list(map(int, input().split()))

    total_score = N[0] + N[1]
    
    if N[0] == -1 and N[1] == -1 and N[2] == -1:
        break
    if N[0] == -1 or N[1] == -1:
        print('F')
    elif total_score >= 80:
        print('A')
    elif 80 > total_score >= 65:
        print('B')
    elif 65 > total_score >= 50:
        print('C')
    elif 50 > total_score >= 30:
        if N[2] >= 50:
            print('C')
        elif 50 > N[2]:
            print('D')
    elif 30 > total_score:
        print('F')
