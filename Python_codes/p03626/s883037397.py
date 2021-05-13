N = int(input())
S1 = input()
S2 = input()
mod = 1000000007
answer = 1
easy = []
i = 0

while N > i:
    if S1[i] == S2[i]:
        easy.append(1)
    else:
        easy.append(0)
        i += 1
    i += 1

for i in range(len(easy)):
    if i == 0:
        if easy[i] == 0:
            answer *= 6
        else:
            answer *= 3
    # elif i == 1:
    #     if easy[i] == 0:
    #         if easy[i-1] == 0:
    #             pass
    #         else:
    #             pass
    #     else:
    #         if easy[i-1] == 0:
    #             pass
    #         else:
    #             pass
    else:
        if easy[i] == 0:
            if easy[i-1] == 0:
                answer *= 3
            else:
                answer *= 2
        else:
            if easy[i-1] == 0:
                answer *= 1
            else:
                answer *= 2

print(answer % mod)
