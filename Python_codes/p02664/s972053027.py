from sys import stdin
def main():
    #入力
    readline=stdin.readline
    t=list(readline().strip())
    for i in range(len(t)):
        if t[i]=="?":
            t[i]="D"
    
    print("".join(t))

if __name__=="__main__":
    main()