def resolve():
    A, B = map(int, input().split())
    ans = 0
    for i in range(A, B+1):
        count = 0
        for j in range(len(str(i))):
            if str(i)[j] == str(i)[(j+1)*-1]:
                count += 1
        if count == len(str(i)):
            ans += 1
    print(ans)
resolve()