def main():
    S = list(input())
    num_stone = 0
    num_paper = 0
    ans = 0
    for c in S:
        if c == 'g':
            if num_paper < num_stone:
                num_paper += 1
                ans += 1
            else:
                num_stone += 1
        else:
            if num_paper < num_stone:
                num_paper += 1
            else:
                num_stone += 1
                ans -= 1
    print(ans)
main()
