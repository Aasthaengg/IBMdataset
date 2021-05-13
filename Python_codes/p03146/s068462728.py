def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def main(s):
    temp = []
    count = 0
    ans = 0
    for i in range(s, 100000000):
        if i == s:
            a = i
        else:
            a = f(temp[count-1])
        
        temp.append(a)
        count += 1

        if a == 4 or a == 2 or a == 1:
            ans = count + 3
            break
    # print(temp)
    print(ans)


if __name__ == "__main__":
    s = int(input())

    main(s)
