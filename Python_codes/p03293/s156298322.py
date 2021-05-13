def role(s:str):
    s0, s1 = s[:len(s)-1], s[len(s)-1]
    return s1 + s0

def main():
    s = input()
    t = input()
    for _ in range(len(t)):
        if s == t:
            print('Yes')
            return
        s = role(s)
    print('No')

if __name__ == "__main__":
    main()
