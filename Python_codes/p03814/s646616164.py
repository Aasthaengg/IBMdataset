def main():
    s = input()
    a = len(s); z = 0
    for i, t in enumerate(s):
        if t == 'A':
            a = min(a, i)
        if t == 'Z':
            z = max(z, i)
    ans = z-a+1
    print(ans)

if __name__ == "__main__":
    main()
