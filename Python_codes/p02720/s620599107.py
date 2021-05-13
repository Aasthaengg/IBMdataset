def main():
    K = int(input())
    ans = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 9
    if K <= count:
        print(ans[K-1])
    else:
        for x in ans:
            mod = x % 10
            base = 10*x + mod

            if mod != 0:
                ans.append(base-1)
                count += 1

            ans.append(base)
            count += 1

            if mod != 9:
                ans.append(base+1)
                count += 1

            if count >= K:
                break
        print(ans[K-1])


if __name__ == "__main__":
    main()
