from string import ascii_lowercase
from collections import Counter

def main():
    S = input()
    N = len(S)
    ans = 100
    c = Counter(list(S))

    if any(val == N for  val in c.values()):
        print(0)
        exit()


    for letter in ascii_lowercase:
        count = 0
        T = S
        while True:
            count += 1
            flag = True
            n = len(T)
            next_T = ""

            for i in range(n-1):
                if letter in T[i:i+2]:
                    next_T += letter
                else:
                    next_T += "#"
                    flag = False

            if flag:
                break
            T = next_T
        ans = min(ans, count)

    print(ans)

if __name__ == "__main__":
    main()