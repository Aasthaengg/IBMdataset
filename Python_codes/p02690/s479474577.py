from sys import stdin
def main():
    #入力
    readline=stdin.readline
    x=int(readline())
    flag=False
    for a in range(-200,201):
        for b in range(-200,201):
            if a**5-b**5==x:
                print(a,b)
                flag=True
                break
        if flag: break

if __name__=="__main__":
    main()