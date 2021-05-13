def main():
    ans = 0
    a,b = map(int,input().split())
    for x in range(a+1):
        for y in range(a+1):
            z = b-x-y
            if 0<=z and z<=a:
                ans += 1



    return ans

print(main())
