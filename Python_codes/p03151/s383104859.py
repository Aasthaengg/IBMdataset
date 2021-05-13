#87 C - Exam and Wizard
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
diff = [a-b for a,b in zip(A,B)]
diff = sorted(diff,reverse = True)
negative_v = [i for i in diff if i < 0]
tot = sum(negative_v)

if sum(A) < sum(B):
    print(-1)
else:
    if tot >= 0:
        print(0)
    else:
        cnt = 0
        for d in diff:
            tot += d
            # tot が正になったら終了
            if tot < 0:
                cnt += 1
            else:
                cnt += 1
                break
        ans = cnt + len(negative_v)
        print(ans)