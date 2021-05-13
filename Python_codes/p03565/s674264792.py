def main():
    s = input()
    t = input()
    lis = []
    for i in range(len(s)-len(t)+1):
        f=True
        for j in range(len(t)):
            if(s[i+j]==t[j] or s[i+j]=="?"):
                continue
            else:
                f=False
                break
        if(f):
            tmp = s[0:i]+t+s[i+len(t):]
            res = ""
            for k in range(len(tmp)):
                if(tmp[k]=="?"):
                    res += "a"
                else:
                    res+=tmp[k]
            lis.append(res)
    if(len(lis)==0):
        print("UNRESTORABLE")
    else:
        print(sorted(lis)[0])


if __name__ == '__main__':
    main()
