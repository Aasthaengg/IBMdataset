import math

N = int(input())

if N < 10:
    print(N)
else:
    ketasu = int(math.log10(N)//1 + 1)
    ans = 9*(ketasu - 1)

    start = [str(4) , str(5)]
    start += [str(9) for _ in range(ketasu - 2)]
    start = int(''.join(map(str, start)))

    if start > N:
        start = [str(9) for _ in range(ketasu-1)]
        start = int(''.join(map(str, start)))

    #print(start)

    for i in range(start,N+1,10**(ketasu - 2)):
        temp_ans = 0
        for j in list(str(i)):
            temp_ans += int(j)

        if temp_ans > ans:
            ans = temp_ans

    print(ans)