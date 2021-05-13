if __name__ == "__main__":
    while True:
        w,h = map(int,input().split())
        if w is not 0 or h is not 0:
            for i in range(w):
                for j in range(h):
                    print("#",end="")
                print("")
            print("")
        else:
            break