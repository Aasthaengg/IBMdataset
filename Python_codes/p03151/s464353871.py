def main2():
    N = int(input())
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]

    if sum(A) < sum(B):
        print(-1)
    else:
        S = sum(A) - sum(B)
        C = [[a, b, b, a - b] for a, b in zip(A, B)] 
        C = sorted(C, key=lambda x:x[3])

        ans = 0
        for i in C:
            a, b, c, d = i

            if d == 0:
                pass
            
            elif d > 0:
                if d <= S:
                    S -= d
                else:
                    ans += 1
            else:
                ans += 1

        print(ans)

if __name__ == "__main__":
    main2()