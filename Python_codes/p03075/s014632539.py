from sys import stdin
def main():
    #入力
    readline=stdin.readline
    li=[int(readline()) for _ in range(5)]
    k=int(readline())

    for i in range(1,5):
        if k<li[i]-li[0]:
            print(":(")
            break
    else:
        print("Yay!")
        
if __name__=="__main__":
    main()