N = int(input())
T = [0 for _ in range(N)]
X = [0 for _ in range(N)]
Y = [0 for _ in range(N)]
count = 0
t = 0
x = 0
y = 0

for i in range(N):
    T[i], X[i], Y[i] = map(int, input().split())
    t = abs(T[i] -t)
    x = abs(X[i] -x)
    y = abs(Y[i] -y)
    if t>= x+y and (t-(x+y))%2 == 0:
        count +=1
    else:
        break
    #     else:
    #         print('No1')
    #         exit()
    # else:
    #     print('No2')
    #     break

print('Yes' if count==N else 'No')