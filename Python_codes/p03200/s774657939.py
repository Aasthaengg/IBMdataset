def main():
    s=input()
    l=0
    man=0
    for i,v in enumerate(s):
        if v == "W":
            man += i-l
            l += 1
    print(man)
    
if __name__ == "__main__":
    main()