def main():
    N = int(input())
    num = [int(input()) for _ in range(5)]
    num.sort()
    temp = 0
    temp = N // num[0]
    if N%num[0] == 0:
        ans = temp
    else:
        ans = temp + 1

    ans += 4
    return ans

print(main()) 

