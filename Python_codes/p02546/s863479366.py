
def resolve():
    S = input()
    ans = S + "es" if S[-1] == "s" else S + "s"
    
    print(ans)


if __name__ == "__main__":
    resolve()