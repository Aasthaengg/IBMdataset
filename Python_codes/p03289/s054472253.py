def main():
    s=input()
    if s[0] == "A":
        if (s[2:-1:]).count("C") == 1:
            for i in s[1:]:
                c = False
                if i == "C" and not c:
                    c = True
                    continue
                elif i == "C" and c:
                    break
                elif i.islower():
                    continue
                else:
                    break
            else:
                print("AC")
                return
    print("WA")
    
if __name__ == "__main__":
    main()