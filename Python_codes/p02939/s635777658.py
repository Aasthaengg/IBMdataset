def myAnswer(S: list) -> int:
    ans = [S.pop(0)]
    flag = False
    for s in S:
        if(flag):
            ans[-1] += s
            flag = False
        elif(ans[-1] == s):
            flag = True
            ans.append(s)
        else:
            ans.append(s)
   
    return len(ans)-1 if(flag==True) else len(ans)


def modelAnswer():
    tmp = 1


def main():
    S = list(input())
    print(myAnswer(S[:]))


if __name__ == '__main__':
    main()
