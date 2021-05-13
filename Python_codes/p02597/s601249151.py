
def main():
    n = int(input())
    c = [i for i in input()]
    ans = 0
    cnt = 0
    cnt2 = 0
    for i in range(n):
        if c[i] =="R":
            cnt += 1
    for i in range(cnt):
        if c[i] == "R":
            cnt2 += 1
    ans = cnt - cnt2
    
    print(ans)


if __name__ == "__main__":
    main()