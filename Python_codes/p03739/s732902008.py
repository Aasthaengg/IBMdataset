def solve():

    n = int(input())
    a = list(map(int, input().split()))

    b = [a[i] for i in range(n)]

   # print(a)
   # print(b)

    #Even
    sum_e = 0
    ans_e = 0

    for i in range(n):
        sum_e += a[i]
        if i%2 == 0:
            if sum_e <= 0:
                ans_e += abs(sum_e) + 1
                sum_e += abs(sum_e) + 1
        else:
            if sum_e >= 0:
                ans_e += abs(sum_e) + 1
                sum_e -= abs(sum_e) + 1

    #Odd
    sum_o = 0
    ans_o = 0

    for i in range(n):
        sum_o += b[i]
        if i%2 == 1:
            if sum_o <= 0:
                ans_o += abs(sum_o) + 1
                sum_o += abs(sum_o) + 1
        else:
            if sum_o >= 0:
                ans_o += abs(sum_o) + 1
                sum_o -= abs(sum_o) + 1

    if ans_o <= ans_e:
        ans = ans_o
    else:
        ans = ans_e


    print(ans)

if __name__ ==  "__main__":
    solve()
