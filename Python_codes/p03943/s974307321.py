from sys import stdin
def main():
    #入力
    readline=stdin.readline
    a,b,c=map(int,readline().split())

    li=[a,b,c]
    li.sort(reverse=True)
    if li[0]==li[1]+li[2]:
        print("Yes")
    else:
        print("No")
if __name__=="__main__":
    main()