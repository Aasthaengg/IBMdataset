if __name__ == '__main__':
    s=input()
    a = int(input())
    ans =""
    for i in range(len(s)):
        if (i+1) % a ==1:
            ans+=s[i]
    if a == 1:
        print(s)
    else:
        print(ans)


