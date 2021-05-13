if __name__ == '__main__':

    s = input()
    
    cnt = 0
    #check1
    r = s[::-1]
    if s == r:
        cnt += 1

    #check2
    n = len(s)
    n2 = (n-1)//2
    ss = s[:n2]
    rr = ss[::-1]
    if ss == rr:
        cnt += 1

    #check3
    n3 = (n+3) //2
    sss = s[n3-1:]
    rrr = sss[::-1]
    if sss == rrr:
        cnt += 1

    if cnt==3 :
        print("Yes")
    else:
        print("No")
