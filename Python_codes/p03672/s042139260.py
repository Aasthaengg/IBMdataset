def main():
    s=input()[:-2]
    while not is_even(s):
        s = s[:-2]
    print(len(s))

def is_even(s):
    half = len(s) // 2
    return s[:half] == s[half:]
    
if __name__ == "__main__":
    main()