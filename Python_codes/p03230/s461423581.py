N = int(input())
if N == 1:
    print("Yes")
    print(2)
    print(1, 1)
    print(1, 1)
elif N == 2:
    print("No")
else:
    for i in range(N):
        if N == i * (i+1)/2:
            Ans = []
            ans =[1]
            for j in range(i-1):
                ans.append(ans[-1]+j+2)
            Ans.append(ans)
            ini, level = 1, 1
            for j in range(1, i+1):
                ans = [ini + k for k in range(level)]
                step, wide, temp = i-j, level, ini+level-1
                while step > 0:
                    ans.append(temp+wide)
                    temp += wide
                    step -= 1
                    wide += 1
                Ans.append(ans)
                ini += level
                level += 1
            print("Yes")
            print(len(Ans))
            for j in range(len(Ans)):
                print(i, " ".join(map(str, Ans[j])))      
            break
    else:
        print("No")