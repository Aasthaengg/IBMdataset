def main():
    ss = list(input())
    n = len(ss)
    ans = [0] * n
    cnt = 0
    for i in range(n):
        if ss[i] == "R":
            cnt += 1
        else:
            even_num = cnt // 2
            odd_num = cnt - even_num
            ans[i] += even_num
            ans[i-1] += odd_num
            cnt = 0
    cnt = 0
    for i in range(n-1, -1, -1):
        if ss[i] == "L":
            cnt += 1
        else:
            even_num = cnt // 2
            odd_num = cnt - even_num
            ans[i] += even_num
            ans[i+1] += odd_num
            cnt = 0
    print(*ans)


if __name__ == "__main__":
    main()
