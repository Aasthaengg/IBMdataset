def main():
    S=input()
    ans=0
    Si=''
    tmp=''
    for s in S:
        tmp += s
        if Si != tmp:
            ans += 1
            Si = tmp
            tmp = ''
    print(ans)

main()
