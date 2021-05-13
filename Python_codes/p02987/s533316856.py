def solve():
    s = input()
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                count += 1
    print('YNeos'[count!=2::2])





if __name__ == '__main__':
    solve()
