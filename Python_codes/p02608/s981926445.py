n = int(input())

def main():
    ans = [0]*(n+1)
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                fn = x**2 + y**2 + z**2 + x*y + y*z + z*x
                if fn > n:
                    break
                else:
                    ans[fn] += 1

    for i in range(1, n+1):
        print(ans[i])

if __name__ == '__main__':
    main()