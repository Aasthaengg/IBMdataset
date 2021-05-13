def main():
    a, b = map(int, input().split())
    ans_w = [["."]*100 for _ in range(50)]
    ans_b = [["#"]*100 for _ in range(50)]
    cnt = 1
    for i in range(0, 50, 2):
        if cnt == a:
            break
        for j in range(0, 100, 2):
            ans_b[i][j] = "."
            cnt += 1
            if cnt == a:
                break
    cnt = 1
    for i in range(1, 50, 2):
        if cnt == b:
            break
        for j in range(0, 100, 2):
            ans_w[i][j] = "#"
            cnt += 1
            if cnt == b:
                break
    print("100 100")
    for i in range(50):
        for j in range(100):
            print(ans_b[i][j], end="")
        print("")
    for i in range(50):
        for j in range(100):
            print(ans_w[i][j], end="")
        print("")
if __name__ == "__main__":
    main()