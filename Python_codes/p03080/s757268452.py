if __name__=="__main__":
    n = input()
    sumA = 0
    sumB = 0
    s = input()
    for i in s:
        if i == 'R':
            sumA += 1
        else:
            sumB += 1
    if sumA > sumB:
        print('Yes')
    else:
        print('No')