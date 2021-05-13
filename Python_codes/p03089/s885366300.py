n = int(input())
new_B = list(map(int, input().split()))
ans = []
cnt = 0

while (cnt < 100000) & (new_B != []):
    B = new_B
    length = len(B)
    new_B = []
    for i in range(1, length + 1):
        if B[-i] < (len(B) - i + 1):
            new_B = [B[-i]] + new_B
        elif B[-i] == (len(B) - i + 1):
            ans.append(B[-i])
            new_B = B[:-i] + new_B
            break
        else:
            print(-1)
            exit()
    cnt += 1


if cnt == 100000:
    print(-1)
else:
    for i in ans[::-1]:
        print(i)
