def main():
    k = int(input())
    a = [1]
    a.append(7 % k)
    [a.append((a[i-1] * 10 + 7) % k) for i in range(2, k+1)]
    for i in range(1, k+1):
        if a[i] == 0:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()
