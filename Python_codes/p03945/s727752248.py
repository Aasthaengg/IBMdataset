def main():
    S = input()
    p = S[0]
    c = 0
    for s in S[1:]:
        if s != p:
            p = s
            c += 1
    print(c)
    
if __name__ == "__main__":
    main()