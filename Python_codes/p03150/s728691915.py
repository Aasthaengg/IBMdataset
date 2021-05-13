def main():
    S = input()
    is_keyence = False
    string = "keyence"

    for i in range(len(string)):
        if S.startswith(string[:i]) and S.endswith(string[i:]):
            is_keyence = True
    
    if is_keyence:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()