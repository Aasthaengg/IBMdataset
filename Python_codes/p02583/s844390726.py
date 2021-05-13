N = int(input())
L_list = list(map(int,input().split()))


counter = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            a = L_list[i]
            b = L_list[j]
            c = L_list[k]
            if a==b or b==c or c==a or a+b<=c or b+c<=a or c+a<=b:
                continue
            counter += 1


print(counter)