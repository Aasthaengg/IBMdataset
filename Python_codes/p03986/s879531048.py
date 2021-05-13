def main():
    S = input()
    cnt = 0
    ans = len(S)
    for s in S:
        if s == 'S':
            cnt += 1
        elif s == 'T':
            if cnt:
                cnt -= 1
                ans -= 2
        else:
            cnt = 0
    
    print(ans)

if __name__ == '__main__':
    main()