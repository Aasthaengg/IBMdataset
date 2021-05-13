

if __name__ == "__main__":
    N = int(input())
    mydict = {}
    ans = 0
    for i in range(N):
        s = list(input())
        S = [str(c) for c in s]
        S.sort()
#        print(S)
        if str(S) in mydict.keys():
            mydict[str(S)] += 1 
        else:
            mydict[str(S)] = 1
#    print(mydict)

    for i in mydict.keys():
        tmp = mydict[i]
        if tmp >= 2:
            ans += tmp*(tmp-1)//2
    print(ans)
