import collections

N = int(input())
A_s = list(map(int, input().split()))

CNT_A = collections.Counter(A_s).most_common()
sorted_A = sorted(CNT_A, reverse=True)


verticle = []
ans = 0


for i in range(len(CNT_A)):
    key = sorted_A[i][0]
    value = sorted_A[i][1]
    
    if (value > 1):
        verticle.append(key)
    

    if (len(verticle) == 1 and value > 3):
        ans = key * key
        break

    elif (len(verticle) >= 2):
        ans = verticle[0] * verticle[1]
        break


print(ans)