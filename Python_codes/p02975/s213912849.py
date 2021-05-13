from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)

try:
    if cnt[0] == N:
        print("Yes")
    else:
        if N % 3 != 0:
            print("No")
        else:
            if cnt.most_common(1)[0][1] == N*2//3 and cnt[0] == N//3:
                print("Yes")
            else:
                x = cnt.most_common(3)
                if x[0][1] == x[1][1] == x[2][1] == N//3:
                    if x[0][0]^x[1][0]^x[2][0] == 0:
                        print("Yes")
                    else:
                        print("No")
                else:
                    print("No")
except:
    print("No")