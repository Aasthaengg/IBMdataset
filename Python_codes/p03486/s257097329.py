def answer(s: str, t: str) -> str:
    return 'Yes' if sorted(s) < sorted(t, reverse=True) else 'No'

def main():
    s = input()
    t = input()
    print(answer(s,t))

if __name__ == '__main__':
    main()