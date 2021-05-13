# B - Sum of Three Integers
def main():
    k, s = map(int, input().split())
    cnt = 0

    for i in range(k+1):
        for j in range(k+1):
            z = s-i-j
            if 0 <= z <= k:
                cnt += 1
    else:
        print(cnt)



if __name__ ==  "__main__":
    main()