def main():
    n,k = map(int,input().split())
    a_list = list(map(int, input().split()))
    ans = 0

    a_list.sort(reverse=True)
    for i in range(k):
        ans += a_list[i]

    return ans

print(main())
