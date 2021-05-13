def solve():
    S = input()
    a = S.find('A')
    z = S.rfind('Z')
    print(z - a + 1)

if __name__ == "__main__":
    solve()