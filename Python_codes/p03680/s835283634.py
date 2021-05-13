N = int(input())
A = [int(input()) for _ in range(N)]
A = list(map(lambda x:x-1, A))
ex = [0]*10**5
light = 0
for i in range(N) :
    if light == 1 :
        print(i)
        exit()
    elif ex[light] == 1 :
        print('-1')
        exit()
    ex[light] = 1
    light = A[light]

print('-1')