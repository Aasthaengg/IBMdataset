def solve():
    S = input()
    if S != S[::-1]:
        print("No")
    else:
        sub = S[:(len(S)-1)//2]
        if sub != sub[::-1]:
            print("No")
        else:
            print("Yes")

if __name__ == "__main__":
    solve()