N = int(input())

if N == 1:
    print('Yes')
    print(2)
    print(1, 1)
    print(1, 1)
else:
    r = int((N*2)**0.5)
    if N*2 == r*(r+1):
        print('Yes')
        print(r+1)
        ans = []

        if r % 2 == 0:
            for i in range(r//2):
                ans.append([j+1+i*(r+1) for j in range(r+1)])
            for i in range(r//2):
                c = [j+1+i*(r+1) for j in range(r+1)]
                ans.append(c[i+1:]+c[:i+1])

        else:
            for i in range(r//2):
                ans.append([j+1+i*(r+1) for j in range(r+1)])

            m = N % (r+1)

            for i in range(r//2):
                c = [j+1+m+i*(r+1) for j in range(r+1)]
                ans.append(c[i+1:]+c[:i+1])

            l = [i+1 for i in range(N)]
            ans.append(l[-m:]+l[:m])

            # print(ans)

        for i in zip(*ans):
            print(r, *i)

    else:
        print('No')
