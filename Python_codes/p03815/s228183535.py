def solve(s):

    tmp = s // 11 * 2
    if s % 11 > 6:
        tmp += 2
    elif 6 >= s % 11 > 0:
        tmp+=1
    return tmp

if __name__ == "__main__":
    x = int(input())
    print(solve(x))