def main():
    N = int(input())
    s = input()
    ans = 0
    temp = 0

    for i in range(1,N):
        if s[i] == 'E':
            ans += 1

    temp = ans
    #print(temp)

    for j in range(1,N):
        if s[j-1] == 'W':
            temp += 1

        if s[j] == 'E':
            temp -=1


        if temp < ans:
            ans = temp
        #print(temp)

    return ans

print(main())
