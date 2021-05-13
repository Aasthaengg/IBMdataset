if __name__=="__main__":
    n = input()
    A = input()
    B = input()
    C = input()
    ans = 0
    for a, b, c in zip(A, B, C):
        if a != b and a != c and b != c:
            ans += 2
        elif a == b and b == c :
            pass
        else:
            ans += 1
    print(ans)