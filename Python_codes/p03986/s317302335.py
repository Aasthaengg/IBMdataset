def main():
    X = input()
    S_COUNT = 0
    delete = 0
    for c in X:
        if c == "S":
            S_COUNT += 1
        else:
            if S_COUNT:
                delete += 2
                S_COUNT -= 1
                
    print(len(X)-delete)
if __name__ == "__main__":
    main()