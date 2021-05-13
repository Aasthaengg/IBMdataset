def main():
    s = input()
    kazu = len(s)
    onelen = 0
    zerolen = 0
    
    for i in range(kazu):
        if s[i] == "1":
            onelen += 1
        else:
            zerolen += 1
    
    print(min(onelen, zerolen) * 2)


if __name__ == "__main__":
    main()