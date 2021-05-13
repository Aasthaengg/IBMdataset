def main():
    S = input()
    ans = "CODEFESTIVAL2016"
    cnt = 0
    for s,a in zip(S,ans):
        if s==a:
            pass
        else:
            cnt += 1
    print(cnt)
    
if __name__ == '__main__':
    main()